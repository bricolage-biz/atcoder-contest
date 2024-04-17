class Animal:
  def __init__(self, name):
    self.name = name
  def name(self):
    return self.name

# pythonのモジュール管理システムでは
# "from ファイル名 import モジュール名"というimport文に書かれているファイル名のファイルを全行実行してしまう。
# これを回避するためには以下のテクニックがある。
if __name__ == '__main__':
  print(__name__)
  print(1)