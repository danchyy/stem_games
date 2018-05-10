import argparse
import requests
from task_pillars.pillars import get_solution
from time import sleep, time
import importlib

headers = {
    "Content-type": "text/plain"
}

# sleep_period = 2

task_problem_id_dict = {
    # "pillars": "4292bf95-9793-48b5-9576-daa6d2685e20"
    "faulty_rocket": "fec8307a-488d-4f24-88b5-97f47db80207"
}


def try_get(problem_id):
    error = True
    url = "https://tech.stemgames.hr/api/competitive/v1/"
    url += problem_id
    while error:
        print("GET REQUEST")
        print("url: " + url)
        print(headers)
        response = requests.get(url=url, headers=headers)
        #sleep(sleep_period)
        print("=========================")
        print("GET RESPONSE")
        print("Response text: ", end="")
        print(response.text)
        json_data = {}
        try:
            json_data = response.json()
        except Exception:
            print("No json in response")
            continue
        error = "error" in json_data
        print("=========================\n")
    return json_data


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
        json_data = {}
        try:
            json_data = response.json()
        except Exception:
            print("No json in response")
            continue
        error = "error" in json_data
        print("=========================")
        print("POST RESPONSE")
        print("Response text: ", end="")
        print(response.text)
        #sleep(sleep_period)
    print("=========================")
    print("\n\n")


def get_get_solution_method(task_name):
    script_name = task_name
    method_name = "get_solution"
    task_package = "task_" + task_name

    # Importing the module from string
    pillars_module = importlib.import_module(task_package + "." + script_name)
    # Retrieving the method from module
    method = getattr(pillars_module, method_name)

    return method


def determine_solving_task():
    """

    :return: name of task with highest number of points
    """
    max_points, max_key = None, None
    for key in task_problem_id_dict:
        problem_id = task_problem_id_dict[key]
        response_for_problem = try_get(problem_id=problem_id)
        available_points = response_for_problem["points_if_correct"]
        print("AVAILABLE POINTS: " + str(available_points) + " FOR KEY: " + key)
        if max_points is None or available_points > max_points:
            max_points = available_points
            max_key = key

    print("BEST TASK IS: " + max_key + " WITH " + str(max_points))
    return max_key


def get_problem_id_and_method():
    best_task_name = determine_solving_task()
    problem_id = task_problem_id_dict[best_task_name]
    get_solution_method = get_get_solution_method(best_task_name)
    return problem_id, get_solution_method


def loop():
    counter = 0
    problem_id, solution_method = get_problem_id_and_method()
    while True:
        start = time()
        counter += 1
        print("CURRENT LOOP: " + str(counter))
        if counter % 10 == 0:
            problem_id, solution_method = get_problem_id_and_method()
        json_data = try_get(problem_id)
        output, submission_id = work_task(json_data, get_solution_method=solution_method)
        post_method(problem_id=problem_id, submission_id=submission_id, solution=output)

        print("TIME: {}\n\n".format(time() - start))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for request/response handling.')
    parser.add_argument('--api', '-a',
                        required=True,
                        help='Team\'s API key')

    # Getting arguments
    args = parser.parse_args()

    # Add api key to header
    headers["Authorization"] = "token " + args.api

    loop()
