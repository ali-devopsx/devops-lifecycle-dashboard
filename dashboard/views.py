# import library to get system info (CPU and RAM)
import psutil

# import library to control Docker from Python
import docker

# import render to show HTML page
from django.shortcuts import render

# import HttpResponse to show logs text
from django.http import HttpResponse


# this function runs when user open /dashboard/
def dashboard_view(request):

    # ==============================
    # CPU usage
    # ==============================

    # get CPU usage percentage
    # interval=1 means wait 1 second for accurate result
    cpu_usage = psutil.cpu_percent(interval=1)


    # ==============================
    # RAM usage
    # ==============================

    # get memory (RAM) details
    memory = psutil.virtual_memory()

    # get RAM usage percentage
    ram_usage = memory.percent


    # ==============================
    # Docker containers
    # ==============================

    try:
        # connect to Docker engine from system
        client = docker.from_env()

        # get all containers (running and stopped)
        containers = client.containers.list(all=True)

        # create empty list to store container data
        container_list = []

        # loop through each container
        for container in containers:

            # add container name and status to list
            container_list.append({
                "name": container.name,     # container name
                "status": container.status  # running / exited
            })

    except Exception as e:
        # if error happens (ex: Docker not running)
        # show error instead of breaking the app
        container_list = [{
            "name": "Error",
            "status": str(e)
        }]


    # ==============================
    # send data to HTML
    # ==============================

    # create dictionary to send data to template
    context = {
        "cpu": cpu_usage,             # CPU usage value
        "ram": ram_usage,             # RAM usage value
        "containers": container_list  # list of containers
    }

    # render HTML page with data
    return render(request, "dashboard/dashboard.html", context)





# function to restart container
def restart_container(request, name):

    # create docker client
    client = docker.from_env()

    try:
        # get container by name
        container = client.containers.get(name)

        # restart container
        container.restart()

    except Exception as e:
        print("Error:", e)

    # go back to dashboard page
    return redirect('/dashboard/')


# function to start a container
def start_container(request, name):

    # connect to docker
    client = docker.from_env()

    try:
        # get container by name
        container = client.containers.get(name)

        # start container
        container.start()

    except Exception as e:
        print("Start error:", e)

    # go back to dashboard
    return redirect('/dashboard/')





# function to stop a container
def stop_container(request, name):

    # connect to docker
    client = docker.from_env()

    try:
        # get container by name
        container = client.containers.get(name)

        # stop container
        container.stop()

    except Exception as e:
        print("Stop error:", e)

    # go back to dashboard
    return redirect('/dashboard/')






# function to show container logs
def container_logs(request, name):

    # connect to docker
    client = docker.from_env()

    try:
        # get container by name
        container = client.containers.get(name)

        # get last logs from container
        logs = container.logs(tail=50).decode("utf-8")

    except Exception as e:
        logs = str(e)

    # show logs in browser
    return HttpResponse("<pre>" + logs + "</pre>")
