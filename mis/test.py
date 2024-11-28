try:
    import pandas as pd
    import snowflake.connector
except ImportError as e:
    missing_packages = [package.strip() for package in str(e).split(' ')]
    
    if 'pandas' in missing_packages:
        print("Pandas is not installed. Installing Pandas...")
        try:
            import pip
            pip._internal.main(["install", "pandas"])
        except AttributeError:
            import subprocess
            subprocess.run(["pip", "install", "pandas"])
        print("Pandas has been successfully installed.")

    if 'snowflake' in missing_packages:
        print("Snowflake-connector-python is not installed. Installing Snowflake...")
        try:
            import pip
            pip._internal.main(["install", "snowflake-connector-python"])
        except AttributeError:
            import subprocess
            subprocess.run(["pip", "install", "snowflake-connector-python"])
        print("Snowflake-connector-python has been successfully installed.")

    # If you have other packages to install, you can add similar logic here

if 'pandas' in locals():
    print("Pandas is already installed. Version:", pd.__version__)

if 'snowflake' in locals():
    print("Snowflake-connector-python is already installed. Version:", snowflake.connector.__version__)