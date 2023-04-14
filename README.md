# phpdoc-trans

A simple command line tool, use OpenAI api for phpdoc translation.


# Installation

`pip install phpdoc-trans`

# Use

You should have an openAPI key for this command.

To generate an openAI API key, while in the [openAI website](https://beta.openai.com), click on your username in the top right corner, then go to "View API keys" and create a key.

After you get the key, you should set environment variable OPENAI_API_KEY={YOUR_API_KEY}

```shell
phpdoc-trans --lang --model --max-tokens --temperature {translate file path}
```
You can use `phpdoc-trans --help` for more information