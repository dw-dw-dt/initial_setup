"""
以下のコードを ~ ディレクトリに作成
①実行 → ②手動でTeXLiveインストール → ③再実行（冪等性あり）
"""
import subprocess
import pathlib
import platform


if __name__ == '__main__':
    tex_ver = 2023
    
    # update & upgrade
    subprocess.run('sudo apt update && sudo apt upgrade -y', shell=True, check=True)

    # install TeXLive
    if not pathlib.Path('/usr/local/texlive').exists():
        pathlib.Path('/usr/local/tex').mkdir(parents = True, exist_ok= True)

        if pathlib.Path('/usr/local/tex/install-tl-unx.tar.gz').exists():
            pass
        else:
            subprocess.run('sudo wget -P /usr/local/tex http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz', shell=True, check=True)
            subprocess.run('cd /usr/local/tex ; sudo tar xvzf install-tl-unx.tar.gz', shell=True, check=True)
        
        print('Please install mannually.')
        print('cd /usr/local/tex/install-tl-****')
        print('sudo ./install-tl')
        exit()

    # version check
    if pathlib.Path(f'/usr/local/texlive/{tex_ver}').exists():
        pass
    else:
        raise ValueError(f'LaTeX ver is not {tex_ver}')
    
    # update .bashrc
    pathlib.Path('.bashrc').touch(exist_ok= True)

    if platform.machine() == 'aarch64':
        cmd = f'export PATH=$PATH:/usr/local/texlive/{tex_ver}/bin/aarch64-linux'
    else:
        cmd = f'export PATH=$PATH:/usr/local/texlive/{tex_ver}/bin/x86_64-linux'

    already_written = False
    with open('.bashrc', 'r') as f:
        for line in f:
            if cmd in line:
                already_written = True
    
    if not already_written:
        shell_cmd = f'echo "{cmd}" >> ~/.bashrc'
        subprocess.run(shell_cmd, shell=True, check=True)

    if pathlib.Path('/usr/local/tex').exists():
        subprocess.run('sudo rm -rf /usr/local/tex', shell=True, check=True)

    # TeXWorks
    subprocess.run('sudo apt install texworks -y', shell=True, check=True)

    # LibreOffice
    subprocess.run('sudo apt install libreoffice -y', shell=True, check=True)
