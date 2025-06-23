from datetime import datetime
from subprocess import run
import subprocess
import logging

# The program currently updates two things 
# 1. system packages
# 2. 
# 3. docker images

hour = datetime.now().hour
logging.basicConfig(
    filename='auto_update.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s %(message)s]'
)


def run_system_updates():
    print("\033[94m[INFO]\033[0m ==== Starting system updates ====", hour)
    logging.info("system updates & upgrades started")
    try:
        # update packages
        logging.info("system update started")
        print("\n\033[94m[INFO]\033[0m ---- Running System Update ----")
        print("\033[93m[CMD]\033[0m sudo apt-get update")
        run("sudo apt-get update", shell=True)
        print("\033[92m[SUCCESS]\033[0m ---- Update Complete ----")
        logging.info("system update successfull")

        # upgrade packages
        logging.info("system upgrade started")
        print("\n\033[94m[INFO]\033[0m ---- Running System Upgrade ----")
        print("\033[93m[CMD]\033[0m sudo apt-get upgrade -y")
        run("sudo apt-get upgrade -y", shell=True)
        print("\033[92m[SUCCESS]\033[0m ---- Upgrade Complete ----")
        logging.info("system upgrade successfull")

        # Cleaning packages
        print("\n\033[94m[INFO]\033[0m ---- Cleaning APT packages ----")
        print("\033[93m[CMD]\033[0m sudo apt-get autoclean -y && sudo apt-get autoremove -y")
        run("sudo apt-get autoclean -y", shell=True)
        run("sudo apt-get autoremove -y", shell=True)
        print("\033[92m[SUCCESS]\033[0m ---- APT Cleaning Complete ----")

        try:
            pass
            # Cleaning snap packages
            print("\n\033[94m[INFO]\033[0m ---- Cleaning Snap packages ----")
            print("\033[93m[CMD]\033[0m sudo snap refresh")
            run("sudo snap refresh", shell=True)
            print("\033[92m[SUCCESS]\033[0m ---- snap Cleaning Complete ----")
        except:
            print("Something went wrong updating snap packages")

    except Exception as e:
        print(f"\033[91m[ERROR]\033[0m Error occurred during system updates: {e}")
     
def update_docker_images():
    print("\n\n")
    print("==== updating docker images ====")
    print("\033[38;5;208mNOTE\033[0m: press [CTRL + C] to stop the download of downloading image and to continue to the next one")
    print("\n\n")
    logging.info("Starting Docker image update process")
    
    # Get a list of all docker images (as text output)
    command = run(['docker', 'images'], capture_output=True, text=True, check=True) # get a llist of all the docker images
    command = command.stdout.splitlines()
    images = [] #store the name of the images here
    images_not_updated = []     # store images that couldn't be updated and require manual handling
    for index, line in enumerate(command):
        if index > 0:
            line = line.strip()
            repo = line.split()[0]
            if repo != "<none>":
                images.append(repo)
   
    # print(images)
    for image in images:    # pull new image from docker repo
        try:
            print(f"\033[94m[INFO]\033[0m Pulling new image for: \033[1m{image}\033[0m")
            logging.info(f"Pulling new image for: {image}")
            # Pull the latest version of the image from Docker Hub
            command = run(["docker", "pull", image], capture_output=True, text=True, check=True)
            command = command.stdout.splitlines()
            # Docker pull output: status is usually on the 4th line (may vary by image)
            if len(command) > 3:
                status = command[3].split(":", 1)
                print(f"\033[92m[SUCCESS]\033[0m {status[1].strip()}")
                logging.info(f"Image {image} updated: {status[1].strip()}")
            else:
                print(f"\033[93m[WARNING]\033[0m Unexpected output format for image: {image}")
                logging.warning(f"Unexpected output format for image: {image}")
            print()
        except subprocess.CalledProcessError:
            print(f"\033[91m[ERROR]\033[0m Error updating image: {image}")
            logging.error(f"Error updating image: {image}")
            images_not_updated.append(image)
            print()

        except KeyboardInterrupt:
            print("\033[93m[WARNING]\033[0m Interrupted by user. Skipping to next image.\n")
            logging.warning(f"Interrupted by user while updating image: {image}")
            continue

        except Exception as e:
            print(f"\033[91m[ERROR]\033[0m Error occurred for image {image}: {e}. Continuing with the rest.\n")
            logging.error(f"Error occurred for image {image}: {e}. Continuing with the rest.")
    # Print images that could not be updated (for manual review)
    if images_not_updated:
        print("\033[91m[ATTENTION]\033[0m These images couldn't be updated and might require manual attention:")
        logging.warning("These images couldn't be updated and might require manual attention:")
        for image in images_not_updated:
            print(f"  - {image}")
            logging.warning(f"  - {image}")
    else:
        print("\033[92m[INFO]\033[0m All images updated successfully!")
        logging.info("All docker images updated successfully!")


def main():
    if hour:# == "0":
        run_system_updates()
        update_docker_images()

        # reboot after everything
        # run("sudo shutdown -h now")


if __name__=="__main__":
    main()

