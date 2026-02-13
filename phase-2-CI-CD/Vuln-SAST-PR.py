import subprocess

@app.route("/run")
def run_cmd():
    cmd = request.args.get("cmd")
    subprocess.run(cmd, shell=True)  # ❌ Command injection
    print ("Command executed: " + cmd)
    return "Done"