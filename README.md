# 算法妈妈垂类大模型生态
## 简介
* 以最高效方式为企业构筑垂类大模型

## Installation

Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```
Modify `constants.py.default` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys), and rename it to `constants.py`.

Place your own data into `data/data.txt`.

## Example usage
Test reading `data/selection/wei.20230701/01/data.html` file
```
> python chatgpt.py "how much is the Jewelry Box"
Your dog's name is Sunny.
```

Test reading `data/data.txt` file.
```
> python chatgpt.py "what is my dog's name"
Your dog's name is Sunny.
```

Test reading `data/cat.pdf` file.
```
> python chatgpt.py "what is my cat's name"
Your cat's name is Muffy.
```
