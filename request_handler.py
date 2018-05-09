import requests
from task_pillars.pillars import get_solution

headers = {
    "Authorization" : "token 5Jx2jthg8uTMUyRK6FoRYagfvEow6wNo"
}

def get_method(problem_id):
    url = "https://tech.stemgames.hr/api/competitive/v1/"
    url += problem_id
    response = requests.get(url=url, headers=headers)
    if not "error" in response.json():
        print(response.text)
    return response.json()

def work_task_pillars(json_data):
    """

    :param json_data:
    :return: Solution and submission ID.
    """
    submission_id = json_data["submission_id"]
    string = json_data["input"]
    output = get_solution(string)
    return output, submission_id

def post_method(problem_id, submission_id, solution):
    url = "https://tech.stemgames.hr/api/competitive/v1/"
    url += problem_id + "/" + submission_id
    params = {"data" : solution}
    response = requests.post(url=url, params=params, headers=headers)
    if not "error" in response.json():
        print(response.text)

def loop(problem_id):
    json_data = get_method(problem_id)
    output, submission_id = work_task_pillars(json_data)
    post_method(problem_id=problem_id, submission_id=submission_id, solution=output)

if __name__ == '__main__':
    loop(problem_id="4292bf95-9793-48b5-9576-daa6d2685e20")