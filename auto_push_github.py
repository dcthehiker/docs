import subprocess

def run_git_commands(path):
    try:
        # 进入对应目录
        subprocess.run(['cd', f'{path}'], check=True)

        # 将所有修改过的文件添加到暂存区
        subprocess.run(['git', 'add', '.'], check=True)
        
        # 提交修改
        subprocess.run(['git', 'commit', '-m', 'Auto commit'], check=True)
        
        # 推送到github
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        
        print("Git commands executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    git_path = '/Users/dachuan/notes/docs'
    run_git_commands(git_path)
