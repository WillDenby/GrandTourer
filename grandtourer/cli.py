import click
import os
import subprocess

def get_applications_dict():
    applications_dict = {}

    # List applications in the /Applications folder
    applications_folder = "/Applications"
    applications_list = os.listdir(applications_folder)
    for app_name in applications_list:
        key = app_name.replace(" ", "").replace(".app", "").lower()
        value = app_name.replace(".app", "")
        applications_dict[key] = value

    # List applications in the /System/Applications folder
    system_applications_folder = "/System/Applications"
    system_applications_list = os.listdir(system_applications_folder)
    for app_name in system_applications_list:
        key = app_name.replace(" ", "").replace(".app", "").lower()
        value = app_name.replace(".app", "")
        applications_dict[key] = value

    return applications_dict

def filter_dict_by_prefix(applications_dict, prefix):
    filtered_dict = {key: value for key, value in applications_dict.items() if key.startswith(prefix)}
    return filtered_dict

def open_application(application_name):
    try:
        # Use the subprocess module to run the open command
        subprocess.run(['open', '-a', application_name], check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"Error opening application: {application_name}")
        click.echo(e)

@click.command(options_metavar='')
@click.argument('application', metavar='APPLICATION...', nargs=-1)
def app(application):
    """Launches your APPLICATION.

    You only need to enter the first few letters. 
    Don't worry about capitals or spaces. 
    String matching will find your application.
    """

    applications_dict = get_applications_dict()

    desired_prefix = ''.join(application).lower()

    result = filter_dict_by_prefix(applications_dict, desired_prefix)
        
    if len(result) == 1:
        for value in result.values():
            open_application(value)
    elif len(result) == 0:
        click.echo("No apps found")
    else:
        click.echo("Did you mean one of the following?")
        for value in result.keys():
            click.echo(value)

if __name__ == '__main__':
    app()

