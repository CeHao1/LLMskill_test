import openai
from utils.file_utils import *
from llm.completor_openai import OpenAICompletor
import time

def main(index):
    api_key = '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'
    openai.api_key = api_key

    prompt = """
    

    """
    t0 = time.time()
    completor = OpenAICompletor()
    ans = completor.answer(prompt)

    t1 = time.time()
    print('time: ', t1 - t0)
    # print(ans)

    mkdir('./results')
    write_txt_file(f'./results/ans{index}.txt', ans)

if __name__ == '__main__':
    import multiprocessing

    tasks=list(range(20))

    with multiprocessing.Pool(processes=4) as pool:
        # Use the map function to apply the worker function to the list of numbers
        pool.map(main, tasks)

