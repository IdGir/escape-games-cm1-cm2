"""Extraits des textes officiels cités dans les consignes de « Le Sceau de la République » (les leçons du jeu sont des PDF : la phrase de
justification se choisit dans le document cité dans la consigne). Textes du domaine public : Déclaration de 1789, Préambule de 1946,
Constitution du 4 octobre 1958, Charte de l'environnement (2004). À vérifier sur Légifrance avant diffusion (voir A-VERIFIER)."""
from aide import carnet

DDHC1 = "Les hommes naissent et demeurent libres et égaux en droits."
DDHC4 = "La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui."
DDHC6 = "La loi est l'expression de la volonté générale."
DDHC11 = "La libre communication des pensées et des opinions est un des droits les plus précieux de l'homme."
DDHC16 = "Toute société dans laquelle la garantie des droits n'est pas assurée, ni la séparation des pouvoirs déterminée, n'a point de Constitution."

P46_1 = "La loi garantit à la femme, dans tous les domaines, des droits égaux à ceux de l'homme."
P46_2 = "La Nation garantit l'égal accès de l'enfant et de l'adulte à l'instruction, à la formation professionnelle et à la culture."
P46_3 = "L'organisation de l'enseignement public gratuit et laïque à tous les degrés est un devoir de l'État."
P46_4 = "Tout homme persécuté en raison de son action en faveur de la liberté a droit d'asile sur les territoires de la République."
P46_5 = "La Nation garantit à tous, notamment à l'enfant, à la mère et aux vieux travailleurs, la protection de la santé, la sécurité matérielle, le repos et les loisirs."

P46_6 = "Chacun a le devoir de travailler et le droit d'obtenir un emploi."

C1 = "La France est une République indivisible, laïque, démocratique et sociale."
C1b = "Elle assure l'égalité devant la loi de tous les citoyens sans distinction d'origine, de race ou de religion."
C2 = "La devise de la République est « Liberté, Égalité, Fraternité »."
C3 = "La souveraineté nationale appartient au peuple qui l'exerce par ses représentants et par la voie du référendum."
C5 = "Le Président de la République veille au respect de la Constitution."
C6 = "Le Président de la République est élu pour cinq ans au suffrage universel direct."
C6b = "Nul ne peut exercer plus de deux mandats consécutifs."
C10 = "Le Président de la République promulgue les lois dans les quinze jours qui suivent la transmission au Gouvernement de la loi définitivement adoptée."
C39 = "L'initiative des lois appartient concurremment au Premier ministre et aux membres du Parlement."
C44 = "Les membres du Parlement et le Gouvernement ont le droit d'amendement."
C45 = "Tout projet ou proposition de loi est examiné successivement dans les deux assemblées du Parlement en vue de l'adoption d'un texte identique."
C61 = "Les lois peuvent être déférées au Conseil constitutionnel, avant leur promulgation, par le Président de la République, le Premier ministre, le président de l'Assemblée nationale, le président du Sénat, soixante députés ou soixante sénateurs."
C62 = "Une disposition déclarée inconstitutionnelle sur le fondement de l'article 61 ne peut être promulguée ni mise en application."
C20 = "Le Gouvernement détermine et conduit la politique de la Nation."
C24 = "Le Parlement vote la loi. Il contrôle l'action du Gouvernement."
C64 = "Le Président de la République est garant de l'indépendance de l'autorité judiciaire."

ENV1 = "Chacun a le droit de vivre dans un environnement équilibré et respectueux de la santé."
ENV2 = "Toute personne a le devoir de prendre part à la préservation et à l'amélioration de l'environnement."


def ddhc(*phr):
    return carnet("Déclaration des droits de l'homme et du citoyen, 1789", " ".join(f"« {p} »" for p in phr))


def preambule(*phr):
    return carnet("Préambule de la Constitution de 1946", " ".join(f"« {p} »" for p in phr))


def c58(*phr):
    return carnet("Constitution du 4 octobre 1958", " ".join(f"« {p} »" for p in phr))


def charte(*phr):
    return carnet("Charte de l'environnement, 2004", " ".join(f"« {p} »" for p in phr))
