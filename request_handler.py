import argparse
import requests
from time import sleep
import importlib

headers = {
    "Content-type": "text/plain"
}


def get_method(problem_id):
    url = "https://tech.stemgames.hr/api/competitive/v1/"
    url += problem_id
    print("GET REQUEST")
    print("url: " + url)
    print(headers)
    response = requests.get(url=url, headers=headers)
    print("=========================")
    print("GET RESPONSE")
    print("Response text: ", end="")
    print(response.text)
    print("=========================\n")
    return response.json()


def work_task(json_data, get_solution_method):
    """

    :param json_data:
    :return: Solution and submission ID.
    """
    submission_id = json_data["submission_id"]
    string = json_data["input"]
    output = get_solution_method(string)
    return output, submission_id


def post_method(problem_id, submission_id, solution):
    url = "https://tech.stemgames.hr/api/competitive/v1/"
    url += problem_id + "/" + submission_id
    print("=========================")
    print("POST REQUEST")
    print("url: " + url)
    print(headers)
    print('SENT SOLUTION: "' + solution + '"')
    error = True
    while error:
        response = requests.post(url=url, data=solution, headers=headers)
        error = "error" in response.json()
        print("=========================")
        print("POST RESPONSE")
        print("Response text: ", end="")
        print(response.text)
        sleep(2)
    print("=========================")
    print("\n\n")


def loop(problem_id, solution_method):
    counter = 0
    while True:
        counter += 1
        print("CURRENT LOOP: " + str(counter))
        json_data = get_method(problem_id)
        sleep(2)
        if "error" in json_data:
            continue
        output, submission_id = work_task(json_data, get_solution_method=solution_method)
        post_method(problem_id=problem_id, submission_id=submission_id, solution=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for request/response handling.')
    parser.add_argument('--api', '-a',
                        required=True,
                        help='Team\'s API key')
    parser.add_argument('--problem', '-p',
                        required=True,
                        help='Problem id')
    parser.add_argument('--task', required=True, help="Name of the task where the script is located")

    # Getting arguments
    args = parser.parse_args()
    script_name = args.task
    method_name = "get_solution"
    task_package = "task_" + args.task

    # Importing the module from string
    pillars_module = importlib.import_module(task_package + "." + script_name)
    # Retrieving the method from module
    method = getattr(pillars_module, method_name)

    # Add api key to header
    headers["Authorization"] = "token " + args.api

    loop(problem_id=args.problem, solution_method=method)
