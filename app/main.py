import subprocess


def run():
    subprocess.run(["streamlit", "run", "app/ui/app.py"])


if __name__ == "__main__":
    run()
