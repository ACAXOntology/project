from rdflib import Graph, URIRef, Namespace, Literal, RDF, OWL, RDFS
import pandas as pd
import re
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore


def create_graph(csv, endpoint, output_name, to_turtle=True, data_delimiter=","):

    data = pd.read_csv(csv, delimiter=data_delimiter)
    endpoint = endpoint + "sparql"

    # Graph
    graph = Graph()
    # Namespaces
    acaxo = Namespace("http://www.semanticweb.org/ACAXO#")
    acaxo_individuals = Namespace("http://www.semanticweb.org/ACAXO/individuals#")
    persp = Namespace(
        "http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#"
    )
    individuals = Namespace("https://github.com/ACAXOntology/")
    mbe = Namespace("https://daselab.org/microblogentry#")

    # Binding namespaces
    graph.bind("acaxo", acaxo)
    graph.bind("persp", persp)
    graph.bind("individuals", individuals)
    graph.bind("acaxo_individuals", acaxo_individuals)
    graph.bind("mbe", mbe)

    graph.remove((None, None, None))

    # NewsEvent
    NewsEvent = URIRef(acaxo.NewsEvent)
    graph.add((NewsEvent, RDF.type, OWL.Class))

    # Attitude
    Attitude = URIRef(persp.Attitude)
    graph.add((Attitude, RDF.type, OWL.Class))

    # Lens
    Lens = URIRef(persp.Lens)
    graph.add((Lens, RDF.type, OWL.Class))

    # Lens <-- BodyChoice
    BodyChoice = URIRef(acaxo.BodyChoice)
    graph.add((BodyChoice, RDF.type, OWL.Class))
    graph.add((BodyChoice, RDFS.subClassOf, persp.Lens))
    # Lens <-- MorallyWrong
    MorallyWrong = URIRef(acaxo.MorallyWrong)
    graph.add((MorallyWrong, RDF.type, OWL.Class))
    graph.add((MorallyWrong, RDFS.subClassOf, persp.Lens))
    # Lens <-- MorallyWrong <-- Sin
    Sin = URIRef(acaxo.Sin)
    graph.add((Sin, RDF.type, OWL.Class))
    graph.add((Sin, RDFS.subClassOf, acaxo.MorallyWrong))
    # Lens <-- WomenEquality
    WomenEquality = URIRef(acaxo.WomenEquality)
    graph.add((WomenEquality, RDF.type, OWL.Class))
    graph.add((WomenEquality, RDFS.subClassOf, persp.Lens))
    # Lens <-- WomenEquality <-- EconomicEquality
    EconomicEquality = URIRef(acaxo.EconomicEquality)
    graph.add((EconomicEquality, RDF.type, OWL.Class))
    graph.add((EconomicEquality, RDFS.subClassOf, acaxo.WomenEquality))
    # Lens <-- WomenEquality <-- Healthcare
    Healthcare = URIRef(acaxo.Healthcare)
    graph.add((Healthcare, RDF.type, OWL.Class))
    graph.add((Healthcare, RDFS.subClassOf, acaxo.WomenEquality))
    # Lens <-- Right
    Right = URIRef(acaxo.Right)
    graph.add((Right, RDF.type, OWL.Class))
    graph.add((Right, RDFS.subClassOf, persp.Lens))
    # Lens <-- AgainstLife
    AgainstLife = URIRef(acaxo.AgainstLife)
    graph.add((AgainstLife, RDF.type, OWL.Class))
    graph.add((AgainstLife, RDFS.subClassOf, persp.Lens))
    # Lens <-- AgainstLife <-- Murder
    Murder = URIRef(acaxo.Murder)
    graph.add((Murder, RDF.type, OWL.Class))
    graph.add((Murder, RDFS.subClassOf, acaxo.AgainstLife))
    # Lens <-- AgainstLife <-- TheUnborn
    TheUnborn = URIRef(acaxo.TheUnborn)
    graph.add((TheUnborn, RDF.type, OWL.Class))
    graph.add((TheUnborn, RDFS.subClassOf, acaxo.AgainstLife))

    # Cut
    Cut = URIRef(persp.Cut)
    graph.add((Lens, RDF.type, OWL.Class))
    # Cut <-- BodyChoice
    AbortionAsBodyChoice = URIRef(acaxo.AbortionAsBodyChoice)
    graph.add((AbortionAsBodyChoice, RDF.type, OWL.Class))
    graph.add((AbortionAsBodyChoice, RDFS.subClassOf, persp.Cut))
    # Cut <-- MorallyWrong
    AbortionIsMorallyWrong = URIRef(acaxo.AbortionAsMorallyWrong)
    graph.add((AbortionIsMorallyWrong, RDF.type, OWL.Class))
    graph.add((AbortionIsMorallyWrong, RDFS.subClassOf, persp.Cut))
    # Cut <-- MorallyWrong <-- Sin
    AbortionIsSin = URIRef(acaxo.AbortionIsSin)
    graph.add((AbortionIsSin, RDF.type, OWL.Class))
    graph.add((AbortionIsSin, RDFS.subClassOf, acaxo.AbortionAsMorallyWrong))
    # Cut <-- WomenEquality
    AbortionForWomenEquality = URIRef(acaxo.AbortionForWomenEquality)
    graph.add((AbortionForWomenEquality, RDF.type, OWL.Class))
    graph.add((AbortionForWomenEquality, RDFS.subClassOf, persp.Cut))
    # Cut <-- WomenEquality <-- EconomicEquality
    AbortionForEconomicEquality = URIRef(acaxo.AbortionForEconomicEquality)
    graph.add((AbortionForEconomicEquality, RDF.type, OWL.Class))
    graph.add((AbortionForEconomicEquality, RDFS.subClassOf, acaxo.AbortionForWomenEquality))
    # Cut <-- WomenEquality <-- Healthcare
    AbortionForHealthcare = URIRef(acaxo.AbortionForHealthcare)
    graph.add((AbortionForHealthcare, RDF.type, OWL.Class))
    graph.add((AbortionForHealthcare, RDFS.subClassOf, acaxo.AbortionForWomenEquality))
    # Cut <-- Right
    AbortionAsRight = URIRef(acaxo.AbortionAsRight)
    graph.add((AbortionAsRight, RDF.type, OWL.Class))
    graph.add((AbortionAsRight, RDFS.subClassOf, persp.Cut))
    # Cut <-- AgainstLife
    AbortionIsAgainstLife = URIRef(acaxo.AbortionIsAgainstLife)
    graph.add((AbortionIsAgainstLife, RDF.type, OWL.Class))
    graph.add((AbortionIsAgainstLife, RDFS.subClassOf, persp.Cut))
    # Cut <-- AgainstLife <-- Murder
    AbortionIsMurder = URIRef(acaxo.AbortionIsMurder)
    graph.add((AbortionIsMurder, RDF.type, OWL.Class))
    graph.add((AbortionIsMurder, RDFS.subClassOf, acaxo.AbortionIsAgainstLife))
    # Cut <-- AgainstLife <-- TheUnborn
    ProtectTheUnborn = URIRef(acaxo.ProtectTheUnborn)
    graph.add((ProtectTheUnborn, RDF.type, OWL.Class))
    graph.add((ProtectTheUnborn, RDFS.subClassOf, acaxo.AbortionIsAgainstLife))

    # Eventuality
    Eventuality = URIRef(persp.Eventuality)
    graph.add((Eventuality, RDF.type, OWL.Class))
    # Eventuality <-- TXAction
    TXAction = URIRef(acaxo.TXAction)
    graph.add((TXAction, RDF.type, OWL.Class))
    graph.add((TXAction, RDFS.subClassOf, persp.Eventuality))
    # Eventuality <-- TXPost
    TXPost = URIRef(acaxo.TXPost)
    graph.add((TXPost, RDF.type, OWL.Class))
    graph.add((TXPost, RDFS.subClassOf, acaxo.TXAction))
    # Eventuality <-- TXHashtag
    TXHashtag = URIRef(acaxo.TXHashtag)
    graph.add((TXHashtag, RDF.type, OWL.Class))
    graph.add((TXHashtag, RDFS.subClassOf, acaxo.TXAction))

    # Agent
    Agent = URIRef(persp.Agent)
    graph.add((Agent, RDF.type, OWL.Class))
    TXUser = URIRef(acaxo.TXUser)
    # Agent <-- TXUser
    graph.add((TXUser, RDF.type, OWL.Class))
    graph.add((TXUser, RDFS.subClassOf, acaxo.Agent))

    # Background
    Background = URIRef(persp.Background)
    graph.add((Background, RDF.type, OWL.Class))
    # Background <-- TXUserInfo
    TXUserInfo = URIRef(acaxo.TXUserInfo)
    graph.add((TXUserInfo, RDF.type, OWL.Class))
    graph.add((TXUserInfo, RDFS.subClassOf, persp.Background))
    # Background <-- TXUserInfo <-- ReligiousBelief
    ReligiousBelief = URIRef(acaxo.ReligiousBelief)
    graph.add((ReligiousBelief, RDF.type, OWL.Class))
    graph.add((ReligiousBelief, RDFS.subClassOf, acaxo.TXUserInfo))
    # Background <-- TXUserInfo <-- PoliticalLeaning
    PoliticalLeaning = URIRef(acaxo.PoliticalLeaning)
    graph.add((PoliticalLeaning, RDF.type, OWL.Class))
    graph.add((PoliticalLeaning, RDFS.subClassOf, acaxo.TXUserInfo))
    # Background <-- TXUserInfo <-- Gender
    Gender = URIRef(acaxo.Gender)
    graph.add((Gender, RDF.type, OWL.Class))
    graph.add((Gender, RDFS.subClassOf, acaxo.TXUserInfo))
    # Background <-- TXUserInfo <-- Education
    Education = URIRef(acaxo.Education)
    graph.add((Education, RDF.type, OWL.Class))
    graph.add((Education, RDFS.subClassOf, acaxo.TXUserInfo))
    # Background <-- TXUserInfo <-- Age
    Age = URIRef(acaxo.Age)
    graph.add((Age, RDF.type, OWL.Class))
    graph.add((Age, RDFS.subClassOf, acaxo.TXUserInfo))

    # Properties
    shotThrough = URIRef(persp.shotThrough)
    graph.add((shotThrough, RDF.type, OWL.ObjectProperty))

    perspectivisedThrough = URIRef(persp.perspectivisedThrough)
    graph.add((perspectivisedThrough, RDF.type, OWL.ObjectProperty))

    perspectivisedAs = URIRef(persp.perspectivisedAs)
    graph.add((perspectivisedAs, RDF.type, OWL.ObjectProperty))

    holds = URIRef(persp.holds)
    graph.add((holds, RDF.type, OWL.ObjectProperty))

    isAboutNews = URIRef(acaxo.isAboutNews)
    graph.add((isAboutNews, RDF.type, OWL.DatatypeProperty))

    hasEducation = URIRef(acaxo.hasEducation)
    graph.add((hasEducation, RDF.type, OWL.ObjectProperty))

    hasGender = URIRef(acaxo.hasGender)
    graph.add((hasGender, RDF.type, OWL.ObjectProperty))

    hasAge = URIRef(acaxo.hasAge)
    graph.add((hasAge, RDF.type, OWL.ObjectProperty))

    hasPoliticalLeaning = URIRef(acaxo.hasPoliticalLeaning)
    graph.add((hasPoliticalLeaning, RDF.type, OWL.ObjectProperty))

    hasReligiousBelief = URIRef(acaxo.hasReligiousBelief)
    graph.add((hasReligiousBelief, RDF.type, OWL.ObjectProperty))

    contains = URIRef(acaxo.contains)
    graph.add((contains, RDF.type, OWL.ObjectProperty))

    writtenBy = URIRef(mbe.writtenBy)
    graph.add((writtenBy, RDF.type, OWL.ObjectProperty))

    hasContent = URIRef(acaxo.hasContent)
    graph.add((hasContent, RDF.type, OWL.DatatypeProperty))

    ontology_individuals = {
        # Lens
        "SinPerspective": URIRef(acaxo_individuals.SinPerspective),
        "WomenEqualityPerspective": URIRef(acaxo_individuals.WomenEqualityPerspective),
        "EconomicEqualityPerspective": URIRef(
            acaxo_individuals.EconomicEqualityPerspective
        ),
        "HealthcarePerspective": URIRef(acaxo_individuals.HealthcarePerspective),
        "RightPerspective": URIRef(acaxo_individuals.RightPerspective),
        "AgainstLifePerspective": URIRef(acaxo_individuals.AgainstLifePerspective),
        "MurderPerspective": URIRef(acaxo_individuals.MurderPerspective),
        "TheUnbornPerspective": URIRef(acaxo_individuals.TheUnbornPerspective),
        "BodyChoicePerspective": URIRef(acaxo_individuals.BodyChoicePerspective),
        "MorallyWrongPerspective": URIRef(acaxo_individuals.MorallyWrongPerspective),
        # Cuts
        "AbortionIsSinPerspective": URIRef(acaxo_individuals.AbortionIsSinPerspective),
        "AbortionForWomenEqualityPerspective": URIRef(
            acaxo_individuals.AbortionForWomenEqualityPerspective
        ),
        "AbortionForEconomicEqualityPerspective": URIRef(
            acaxo_individuals.AbortionForEconomicEqualityPerspective
        ),
        "AbortionForHealthcarePerspective": URIRef(
            acaxo_individuals.AbortionForHealthcarePerspective
        ),
        "AbortionAsRightPerspective": URIRef(acaxo_individuals.AbortionAsRightPerspective),
        "AbortionIsAgainstLifePerspective": URIRef(
            acaxo_individuals.AbortionIsAgainstLifePerspective
        ),
        "AbortionIsMurderPerspective": URIRef(
            acaxo_individuals.AbortionIsMurderPerspective
        ),
        "ProtectTheUnbornPerspective": URIRef(
            acaxo_individuals.ProtectTheUnbornPerspective
        ),
        "AbortionAsBodyChoicePerspective": URIRef(
            acaxo_individuals.AbortionAsBodyChoicePerspective
        ),
        "AbortionIsMorallyWrongPerspective": URIRef(
            acaxo_individuals.AbortionIsMorallyWrongPerspective
        ),
        "AbortionAsBodyChoicePerspective": URIRef(
            acaxo_individuals.AbortionAsBodyChoicePerspective
        ),
        "AbortionIsMorallyWrongPerspective": URIRef(
            acaxo_individuals.AbortionIsMorallyWrongPerspective
        ),
        "Neutral": URIRef(acaxo_individuals.Neutral),
        "ProChoice": URIRef(acaxo_individuals.ProChoice),
        "ProLife": URIRef(acaxo_individuals.ProLife),
        "HighschoolOrLower": URIRef(acaxo_individuals.HighschoolOrLower),
        "CollegeOrHigher": URIRef(acaxo_individuals.CollegeOrHigher),
        "Female": URIRef(acaxo_individuals.Female),
        "Male": URIRef(acaxo_individuals.Male),
        "Liberal": URIRef(acaxo_individuals.Liberal),
        "Conservative": URIRef(acaxo_individuals.Conservative),
        "Religious": URIRef(acaxo_individuals.Religious),
        "NotReligious": URIRef(acaxo_individuals.NotReligious),
        "AgeUnder20": URIRef(acaxo_individuals.AgeUnder20),
        "Age20To30": URIRef(acaxo_individuals.Age20To30),
        "Age30To40": URIRef(acaxo_individuals.Age30To40),
        "Age40To50": URIRef(acaxo_individuals.Age40To50),
        "Age50To60": URIRef(acaxo_individuals.Age50To60),
        "AgeAbove60": URIRef(acaxo_individuals.AgeAbove60),
    }

    # instantiate lens
    graph.add((ontology_individuals["SinPerspective"], RDF.type, Sin))
    graph.add(
        (ontology_individuals["WomenEqualityPerspective"], RDF.type, WomenEquality)
    )
    graph.add(
        (
            ontology_individuals["EconomicEqualityPerspective"],
            RDF.type,
            EconomicEquality,
        )
    )
    graph.add((ontology_individuals["HealthcarePerspective"], RDF.type, Healthcare))
    graph.add((ontology_individuals["RightPerspective"], RDF.type, Right))
    graph.add((ontology_individuals["AgainstLifePerspective"], RDF.type, AgainstLife))
    graph.add((ontology_individuals["MurderPerspective"], RDF.type, Murder))
    graph.add((ontology_individuals["TheUnbornPerspective"], RDF.type, TheUnborn))
    graph.add(
        (
            ontology_individuals["BodyChoicePerspective"],
            RDF.type,
            BodyChoice,
        )
    )
    graph.add(
        (
            ontology_individuals["MorallyWrongPerspective"],
            RDF.type,
            MorallyWrong,
        )
    )

    # instantiate cuts
    graph.add(
        (ontology_individuals["AbortionIsSinPerspective"], RDF.type, AbortionIsSin)
    )
    graph.add(
        (
            ontology_individuals["AbortionForWomenEqualityPerspective"],
            RDF.type,
            AbortionForWomenEquality,
        )
    )
    graph.add(
        (
            ontology_individuals["AbortionForEconomicEqualityPerspective"],
            RDF.type,
            AbortionForEconomicEquality,
        )
    )
    graph.add(
        (
            ontology_individuals["AbortionForHealthcarePerspective"],
            RDF.type,
            AbortionForHealthcare,
        )
    )
    graph.add(
        (
            ontology_individuals["AbortionAsRightPerspective"],
            RDF.type,
            AbortionAsRight,
        )
    )
    graph.add(
        (
            ontology_individuals["AbortionIsAgainstLifePerspective"],
            RDF.type,
            AbortionIsAgainstLife,
        )
    )
    graph.add(
        (
            ontology_individuals["AbortionIsMurderPerspective"],
            RDF.type,
            AbortionIsMurder,
        )
    )
    graph.add(
        (
            ontology_individuals["ProtectTheUnbornPerspective"],
            RDF.type,
        ProtectTheUnborn,
        )
    )
    graph.add(
        (
            ontology_individuals["AbortionAsBodyChoicePerspective"],
            RDF.type,
            AbortionAsBodyChoice,
        )
    )
    graph.add(
        (
            ontology_individuals["AbortionIsMorallyWrongPerspective"],
            RDF.type,
            AbortionIsMorallyWrong,
        )
    )

    # instantiate attitude
    graph.add((
        ontology_individuals["Neutral"],
        RDF.type,
        Attitude
    ))
    graph.add((ontology_individuals["ProChoice"], RDF.type, Attitude))
    graph.add((ontology_individuals["ProLife"], RDF.type, Attitude))
    # instantiate information about the user
    graph.add((ontology_individuals["HighschoolOrLower"], RDF.type, Education))
    graph.add((ontology_individuals["CollegeOrHigher"], RDF.type, Education))

    graph.add((ontology_individuals["Male"], RDF.type, Gender))
    graph.add((ontology_individuals["Female"], RDF.type, Gender))

    graph.add((ontology_individuals["Liberal"], RDF.type, PoliticalLeaning))
    graph.add((ontology_individuals["Conservative"], RDF.type, PoliticalLeaning))

    graph.add((ontology_individuals["Religious"], RDF.type, ReligiousBelief))
    graph.add((ontology_individuals["NotReligious"], RDF.type, ReligiousBelief))

    # instantiate posts
    post_instances = {
        row["id"]: URIRef(individuals + "TXPost_" + str(row["id"]))
        for idx, row in data.iterrows()
    }

    for _, value in post_instances.items():
        graph.add((value, RDF.type, TXPost))

    # conversion from cut to lens
    def from_cut_to_lens(original_string):
        # Remove "Abortion" and keep only the second part
        cleaned_string = original_string.replace("Abortion", "", 1)
        # Remove prefixes like "Is" or "For" if they are present
        return re.sub(r"^(Is|For|As|Protect)", "", cleaned_string)

    for idx, row in data.iterrows():
        post_uri = post_instances[row["id"]]
        # adding the text of the post
        text = row["post_text"]
        graph.add((post_uri, hasContent, Literal(text)))
        # connectin to news
        if not pd.isna(row["news"]) and row["news"].lower() != 'no':
            graph.add((post_uri, isAboutNews, Literal(row["news"])))
        # creating connections with lens and cuts
        post_lens = [
            from_cut_to_lens(cut.strip() + "Perspective")
            for cut in row["cut_post"].split(",")
        ]
        post_cut = [
            cut.strip() + "Perspective"
            for cut in row["cut_post"].split(",")
        ]
        # connect post with lens
        for lens in post_lens:
            if lens in ontology_individuals:
                graph.add((post_uri, shotThrough, ontology_individuals[lens]))
            else:
                print(f"Warning: '{lens}' not found in ontology_individuals")
        # connect post with cut
        for cut in post_cut:
            if cut in ontology_individuals:
                graph.add((post_uri, perspectivisedAs, ontology_individuals[cut]))
            else:
                print(f"Warning: '{cut}' not found in ontology_individuals")

    # instantiate hashtag
    hashtag_instances = {
        row["id"]: URIRef(individuals + "TXHashtag_" + str(row["id"]))
        for idx, row in data.iterrows()
    }

    for _, value in hashtag_instances.items():
        graph.add((value, RDF.type, TXHashtag))

    # connecting posts with hashtags
    for key, value in post_instances.items():
        graph.add((value, contains, hashtag_instances[key]))

    # creating connections with lens and cuts
    for idx, row in data.iterrows():
        hashtag_uri = hashtag_instances[row["id"]]
        # connecting hashtags with their text
        text = row["hashtag_text"]
        graph.add((hashtag_uri, hasContent, Literal(text)))
        # creating connections with lens and cuts
        hashtag_lens = [
            from_cut_to_lens(cut.strip() + "Perspective")
            for cut in row["cut_post"].split(",")
        ]
        hashtag_cut = [cut.strip() + "Perspective" for cut in row["cut_post"].split(",")]
        # connect post with lens
        for lens in hashtag_lens:
            if lens in ontology_individuals:
                graph.add((hashtag_uri, shotThrough, ontology_individuals[lens]))
            else:
                print(f"Warning: '{lens}' not found in ontology_individuals")
        # connect post with cut
        for cut in hashtag_cut:
            if cut in ontology_individuals:
                graph.add((hashtag_uri, perspectivisedAs, ontology_individuals[cut]))
            else:
                print(f"Warning: '{cut}' not found in ontology_individuals")

    # instantiate users
    user_instances = {
        row["id"]: URIRef(individuals + "TXUser_" + str(row["id"]))
        for idx, row in data.iterrows()
    }
    for _, value in user_instances.items():
        graph.add((value, RDF.type, TXUser))

    # connecting posts with users
    for key, value in post_instances.items():
        graph.add((value, writtenBy, user_instances[key]))

    def to_camel_case(text):
        removed = text.replace('-', ' ').replace('_', ' ').split()
        if len(removed) == 0:
            return ''
        return ''.join([x.capitalize() for x in removed])

    for idx, row in data.iterrows():
        user_uri = user_instances[row["id"]]
        # connect user position
        if not pd.isna(row["position"]):
            position = row["position"]
            graph.add((user_uri, holds, ontology_individuals[position]))
        # connect user gender
        if "gender" in row and not pd.isna(row["gender"]):
            gender = row["gender"].lower().capitalize()
            graph.add((user_uri, hasGender, ontology_individuals[gender]))
        if "age" in row and not pd.isna(row["age"]):
            age = 'Age' + to_camel_case(row["age"])
            graph.add((user_uri, hasAge, ontology_individuals[age]))
        # connect user education
        if "education" in row and not pd.isna(row["education"]):
            education = 'CollegeOrHigher' if 'college' in row["education"].lower() else "HighschoolOrLower"
            graph.add((user_uri, hasEducation, ontology_individuals[education]))
        if "political_leaning" in row and not pd.isna(row["political_leaning"]):
            political_lean = row["political_leaning"].lower().capitalize()
            graph.add((user_uri, hasPoliticalLeaning, ontology_individuals[political_lean]))
        if "religious_belief" in row and not pd.isna(row["religious_belief"]):
            religious_belief = "NotReligious" if 'not' in row["religious_belief"].lower() else 'Religious'
            graph.add(
                (user_uri, hasReligiousBelief, ontology_individuals[religious_belief])
            )

    # OPTIONAL: add perspectivazation graph
    # creates problems with SPARQL!!!
    # persp_graph = Graph()
    # persp_graph.parse("perspectivazation.ttl", format="turtle")
    # graph += persp_graph

    store = SPARQLUpdateStore()
    store.open((endpoint, endpoint))

    for triple in graph.triples((None, None, None)):
        store.add(triple)

        store.close()

    if to_turtle:
        # Export to Turtle format and save to a file
        with open(f"{output_name}.ttl", "w") as f:
            f.write(graph.serialize(format="turtle"))


