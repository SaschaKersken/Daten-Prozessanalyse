import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer

texts = ["Künstliche Intelligenz ist eine Sammelbezeichnung für Algorithmen, die Probleme lösen, für die Menschen Intelligenz benötigen. Ob man die Programme selbst als intelligent ansehen kann, ist umstritten. Typische Lösungen gehören zum Gebiet des Machine Learning, bei dem der Algorithmus aus den vorliegenden Daten lernt, wie sie zu interpretieren sind.",
 "Beim Machine Learning, einem wichtigen Teilgebiet der künstlichen Intelligenz, unterscheidet man zwischen überwachtem und unüberwachtem Lernen - je nachdem, ob der Algorithmus zuerst mit Trainingsdaten gewissermaßen kalibriert wird, oder ob man ihn gleich auf die echten Daten loslässt.",
 "Die bekannten Forscher und Buchautoren Russell und Norvig teilen künstliche Intelligenz in vier verschiedene Felder ein: Menschliches Denken, menschliches Handeln, rationales Denken und rationales Handeln. Typische Algorithmen im Machine Learning gehören dabei am ehesten zum rationalen Denken.",
 "Seit Jahrhunderten streitet sich die Forschung darüber, ob menschliche Intelligenz angeboren ist, durch Erziehung und Bildung erworben wird, oder ob es sich um eine Mischung aus beidem handelt. Die beliebten IQ-Tests sind jedenfalls nur sehr bedingt geeignet, ein echtes Maß für menschliche Intelligenz zu bilden, denn das Abschneiden in diesen Tests lässt sich gezielt trainieren."]

text_data = np.array(texts)
hv = HashingVectorizer(n_features = 20)
features = hv.transform(text_data).toarray()
print(features)
