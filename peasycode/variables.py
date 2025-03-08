def main() -> None:
  import CODTAB
  ans = input("<NAME> ")
  data = input("<DATATYPE> ")
  val = input("<VALUE> ")
  index = input("<INDEX> ")
  CODTAB.codtab.insert(index, f'{ans}: {data} = {val}')
