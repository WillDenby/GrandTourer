import click
import os
import subprocess

def get_applications_dict():

    applications_dict = {}
    common_first_words = []
    folders = ["/Applications", "/System/Applications", "/System/Applications/Utilities"]

    for folder in folders:
        applications_list = os.listdir(folder)

        first_words = [app.split()[0] for app in applications_list]
        for word in first_words:
            if first_words.count(word) > 1 and word not in common_first_words:
                common_first_words.append(word)

        for app_name in applications_list:
            key = app_name.replace(" ", "").replace(".app", "").lower()
            value = app_name.replace(".app", "")
            applications_dict[key] = value

    cleaned_dict = {}
    for original_key, value in applications_dict.items():
        key = original_key
        for word in common_first_words:
            if key.lower().startswith(word.lower()):
                key = key[len(word):].lstrip()
                break  # Break once the first common word is removed
        cleaned_dict[key] = value

    return cleaned_dict

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
        for value in result.values():
            click.echo(value)

if __name__ == '__main__':
    app()


