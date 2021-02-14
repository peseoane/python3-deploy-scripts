# GNU LESSER GENERAL PUBLIC LICENSE
# AUTHOR: PEDRO VICENTE SEOANE PRADO (SPAIN)
# https://github.com/peseoane/python3-deploy-scripts/

import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install -U pip wheel setuptools --upgrade ", shell=True)
call("pip install -U --upgrade " + " ".join(packages), shell=True)

packages = [
    "pip install -U spacy",
    "pip install -U spacy[transformers,lookups,ja] --upgrade",
    "pip install -U spacy[cuda80,transformers,lookups,ja] --upgrade",
    "pip install -U spacy[cuda92,transformers,lookups,ja] --upgrade",
    "pip install -U spacy[cuda102,transformers,lookups,ja] --upgrade",
    "pip install -U spacy[cuda110,transformers,lookups,ja] --upgrade",
    "pip install -U spacy[cuda80] --upgrade",
    "pip install -U spacy[cuda92] --upgrade",
    "pip install -U spacy[cuda102] --upgrade",
    "pip install -U spacy[cuda110] --upgrade",
    "python -m spacy download zh_core_web_sm --upgrade",
    "python -m spacy download da_core_news_sm --upgrade",
    "python -m spacy download nl_core_news_sm --upgrade",
    "python -m spacy download en_core_web_sm --upgrade",
    "python -m spacy download fr_core_news_sm --upgrade",
    "python -m spacy download de_core_news_sm --upgrade",
    "python -m spacy download el_core_news_sm --upgrade",
    "python -m spacy download it_core_news_sm --upgrade",
    "python -m spacy download ja_core_news_sm --upgrade",
    "python -m spacy download lt_core_news_sm --upgrade",
    "python -m spacy download mk_core_news_sm --upgrade",
    "python -m spacy download xx_ent_wiki_sm --upgrade",
    "python -m spacy download nb_core_news_sm --upgrade",
    "python -m spacy download pl_core_news_sm --upgrade",
    "python -m spacy download pt_core_news_sm --upgrade",
    "python -m spacy download ro_core_news_sm --upgrade",
    "python -m spacy download ru_core_news_sm --upgrade",
    "python -m spacy download es_core_news_sm --upgrade",
    "python -m spacy download zh_core_web_trf --upgrade",
    "python -m spacy download da_core_news_lg --upgrade",
    "python -m spacy download nl_core_news_lg --upgrade",
    "python -m spacy download en_core_web_trf --upgrade",
    "python -m spacy download fr_dep_news_trf --upgrade",
    "python -m spacy download de_dep_news_trf --upgrade",
    "python -m spacy download el_core_news_lg --upgrade",
    "python -m spacy download it_core_news_lg --upgrade",
    "python -m spacy download ja_core_news_lg --upgrade",
    "python -m spacy download lt_core_news_lg --upgrade",
    "python -m spacy download mk_core_news_lg --upgrade",
    "python -m spacy download xx_sent_ud_sm --upgrade",
    "python -m spacy download nb_core_news_lg --upgrade",
    "python -m spacy download pl_core_news_lg --upgrade",
    "python -m spacy download pt_core_news_lg --upgrade",
    "python -m spacy download ro_core_news_lg --upgrade",
    "python -m spacy download ru_core_news_lg --upgrade",
    "python -m spacy download es_dep_news_trf --upgrade",
]

selected_packages = list()
avaiable_locales = [
    "da",
    "de",
    "el",
    "en",
    "es",
    "fr",
    "it",
    "ja",
    "lt",
    "mk",
    "nb",
    "nl",
    "pl",
    "pt",
    "ro",
    "ru",
    "xx",
    "xh",
]

flag_trained = False
while flag_trained is False:
    try:
        print("\n##### INSTALLING SPACY #####\n")
        print("¿Install trained models?")
        trained = input("Y/n: ")
        if trained.lower() not in ["y", "n"]:
            print("ERROR: Select Y or n")
        else:
            flag_trained = True
    except:
        pass

flag_cuda = False
while flag_cuda is False:
    try:
        print("¿Install CUDA support?")
        cuda = input("Y/n: ")
        if cuda.lower() == "y":
            flag_cuda = True
            cuda_support = True
        elif cuda.lower() == "n":
            flag_cuda = True
            cuda_support = False
        else:
            print("ERROR: Select Y or n")
    except:
        pass

flag_locale = False
while flag_locale is False:
    try:
        print("Input your language from \n%s" % avaiable_locales)
        locale = input("LOCALE: ")
        if locale in avaiable_locales:
            flag_locale = True
        else:
            print("ERROR: Select an avaiable locale from the list")
    except:
        pass

for package in packages:
    if trained.lower() == ("y"):
        if cuda_support:
            if "cuda" and "transformers" in package:
                selected_packages.append(package)
        else:
            if "transformers" in package and "cuda" not in package:
                selected_packages.append(package)
    elif trained.lower() == ("n"):
        if cuda_support:
            if "cuda" in package and not "transformers" in package:
                selected_packages.append(package)
        else:
            if "-U spacy" in package and not "transformers" and not "cuda" in package:
                selected_packages.append(package)

    if locale in package:
        selected_packages.append(package)

flag_install = False
while flag_install is False:
    auth = input(
        "Se instalarán los siguientes paquetes: Y/n: \n%s\n" % selected_packages
    )
    if auth.lower() == "y":
        for package in selected_packages:
            call("%s" % package, shell=True)

    elif auth.lower() == "n":
        print("Instalación cancelada")

    else:
        print("ERROR: Introduzca Y/n")
