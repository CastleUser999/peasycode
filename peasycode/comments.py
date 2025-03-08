def main() -> None:
  import CODTAB
  ans = input("<STRING> ")
  index = input("<INDEX> ")
  CODTAB.codtab.insert(index, f'# {ans}')
