import click
import openai
import os
from bs4 import BeautifulSoup
from .spinner import Spinner

@click.command()
@click.argument('doc', type=click.File('rb'))
@click.option('--lang', default='zh', help='Language to translate')
@click.option('--model', default='text-davinci-003', help='Model ID')
@click.option('--max-tokens', default=100, help='Maximum number of tokens to generate')
@click.option('--temperature', default=0.3, help='Sampling temperature')
def main(doc, lang, model, max_tokens, temperature):
    '''Load phpdoc file and translate it.'''
    # check api key
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        click.echo(
            "No API key provided. You can set the environment variable OPENAI_API_KEY=<API-KEY>")
        return
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # language dict
    languages = {'zh': 'Chinese', 'en': 'English'}
    target_language = languages.get('zh')
    if False == (lang in languages):
        click.echo("Un supported language: " +
                   lang + ". Now supported: zh,en.")
        return
    else:
        trans_sentences = parse_xml2translate_text(doc)
        trans_count = len(trans_sentences)
        if trans_count == 0:
            click.echo("Not find translate tragets")
            return

        # Result dict. key is origin sentence, value is translated sentence
        trans_result = {}
        with Spinner("Translating "):
            for sentence in trans_sentences:
                '''build translate promot'''
                prompt = build_trans_prompt(sentence, target_language)
                tranlated = reqeust_openai(
                    model=model, prompt=prompt, max_tokens=max_tokens, temperature=temperature)
                trans_result[sentence] = tranlated
        
        output_results(trans_result=trans_result)
        return


def output_results(trans_result):
    click.echo()
    click.echo("Successfully translated")
    click.echo("\n")
    for key in trans_result:
        click.echo(key)
        click.echo(trans_result[key])
        click.echo()


'''Build trans prompt for openai'''


def build_trans_prompt(text, language):
    prompt = "Translate this into " + language + ":" + text
    return prompt


'''Parse xml to translate text'''


def parse_xml2translate_text(file):
    file_str = file.read()

    trans_sentences = []
    soup = BeautifulSoup(file_str, 'xml')
    names = soup.find_all('para')
    for name in names:
        new = name.text.strip()
        res = new.replace('\n ', '').replace('  ', '')
        if len(res) > 0:
            trans_sentences.append(res)

    return trans_sentences


'''Async translate'''


async def async_translate(model, target_language, max_tokens, temperature, sentences):
    trans_result = []
    for sentence in sentences:
        '''build translate promot'''
        prompt = build_trans_prompt(sentence, target_language)
        tranlated = await reqeust_openai(model=model, prompt=prompt, max_tokens=max_tokens, temperature=temperature)
        trans_result.append(tranlated)
    return trans_result

'''Request openai'''


def reqeust_openai(model, prompt, max_tokens, temperature):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    if completions.choices:
        return completions.choices[0].text.strip()
    else:
        click.echo('Failed to translate.')


if __name__ == '__main__':
    main()
