import argparse

my_parse = argparse.ArgumentParser(description="CLI para baixar hq's.")

my_parse.add_argument("--search", action="store", type=str, help="Pesquisar.")
my_parse.add_argument("--url", action="store", type=str, help="Url da hq.")
my_parse.add_argument("--output", action="store", type=str, help="Nome de saida do pdf.")
my_parse.add_argument("--option", action="store", type=int, help="Opção da pesquisa.")
my_parse.add_argument("--not-pdf", action="store", type=bool, help="Salva apenas as imagens.", default=False)
my_parse.add_argument("--cap", action="store", type=list, help="Define os capitulos.")

args = my_parse.parse_args()

print(args)