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
                break  
        cleaned_dict[key] = value

    applications_dict.update(cleaned_dict)
    
    return applications_dict

def filter_dict_by_prefix(applications_dict, prefix):
    filtered_dict = {key: value for key, value in applications_dict.items() if key.startswith(prefix)}
    return filtered_dict

def open_application(application_name):
    try:
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
    You can also miss out common first words like "Microsoft" or "Adobe".
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
        options = list(result.values())
        for i, value in enumerate(options, start=1):
            click.echo(f"{i}. {value}")

        selected_option = click.prompt("Enter the number you want. Enter any other number to exit", type=int)

        if 1 <= selected_option <= len(options):
            open_application(options[selected_option - 1])

        else:
            click.echo("Hmm, that wasn't one of the options!")

if __name__ == '__main__':
    app()


