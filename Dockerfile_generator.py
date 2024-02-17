def generate_dockerfile(requirements_file, dockerfile_path):
    with open(requirements_file, 'r') as f:
        requirements = f.readlines()
    
    with open(dockerfile_path, 'w') as f:
        f.write("FROM python:3.9\n\n")
        f.write("WORKDIR /app\n\n")
        f.write("COPY . /app\n\n")
        f.write("RUN pip install --no-cache-dir \\\n")
        
        for requirement in requirements:
            requirement = requirement.strip()
            if requirement:
                f.write(f"    {requirement} \\\n")
        
        f.write("    && rm -rf /var/cache/apt/* /var/cache/yum/* /var/cache/apk/*\n\n")
        f.write("CMD [\"python\", \"app.py\"]\n")

generate_dockerfile("requirements.txt", "Dockerfile")