# MenuTitle: Generate deva OT features
# By Andres Torresi for HuertaTipografica.com
# utiliza los anchos de los glifos en la capa 0 (layers[0])

classes = True
features = True
prefix = True

import GlyphsApp

font = Glyphs.font

presList = [
    ("k-deva", "s-deva", "p_ra-deva"),
    ("k-deva", "s-deva", "p-deva", "la-deva"),
    ("t-deva", "s-deva", "n-deva", "ya-deva"),
    ("n-deva", "s-deva", "m-deva", "ya-deva"),
    ("n-deva", "s_t_ra-deva"),
    ("t-deva", "s_t_ra-deva"),
    ("bh_ra-deva", "ya-deva"),
    ("c-deva", "c-deva", "ya-deva"),
    ("d_da-deva", "va-deva"),
    ("da-deva", "dh_ra-deva"),
    ("da-deva", "v_ra-deva"),
    ("g-deva", "bh-deva", "ya-deva"),
    ("g-deva", "d_va-deva"),
    ("g-deva", "dh-deva", "va-deva"),
    ("g-deva", "dh-deva", "ya-deva"),
    ("g-deva", "l-deva", "ya-deva"),
    ("g-deva", "m-deva", "ya-deva"),
    ("g_n-deva", "ya-deva"),
    ("g_ra-deva", "ya-deva"),
    ("gh-deva", "l-deva", "ya-deva"),
    ("h-deva", "m-deva", "ya-deva"),
    ("k-deva", "k-deva", "ya-deva"),
    ("k-deva", "p_ra-deva"),
    ("k-deva", "s-deva", "dda-deva"),
    ("k-deva", "s-deva", "pa-deva"),
    ("k-deva", "s-deva", "ta-deva"),
    ("k-deva", "s-deva", "tta-deva"),
    ("k_ss-deva", "va-deva"),
    ("k-deva", "t_ra-deva"),
    ("k-deva", "t-deva", "va-deva"),
    ("k-deva", "t-deva", "ya-deva"),
    ("k-deva", "v-deva", "ya-deva"),
    ("kh-deva", "m-deva", "ya-deva"),
    ("kh-deva", "t-deva", "ya-deva"),
    ("l-deva", "d_ra-deva"),
    ("l-deva", "h_ya-deva"),
    ("l-deva", "k-deva", "ya-deva"),
    ("l-deva", "l-deva", "ya-deva"),
    ("l-deva", "th-deva", "ya-deva"),
    ("m-deva", "b_ra-deva"),
    ("m-deva", "b-deva", "ya-deva"),
    ("m-deva", "bh_ra-deva"),
    ("m-deva", "bh-deva", "va-deva"),
    ("m-deva", "bh-deva", "ya-deva"),
    ("m-deva", "m-deva", "ya-deva"),
    ("m-deva", "p_ra-deva"),
    ("n-deva", "bh-deva", "va-deva"),
    ("n-deva", "bh-deva", "ya-deva"),
    ("n-deva", "d_dha-deva"),
    ("n-deva", "d_ra-deva"),
    ("n-deva", "d_va-deva"),
    ("n-deva", "dh_ra-deva"),
    ("n-deva", "dh-deva", "ya-deva"),
    ("n-deva", "g-deva", "va-deva"),
    ("n-deva", "h_ra-deva"),
    ("n-deva", "h_ya-deva"),
    ("n-deva", "j-deva", "ya-deva"),
    ("n-deva", "k_ra-deva"),
    ("n-deva", "k-deva", "sa-deva"),
    ("n-deva", "k_ssa-deva"),
    ("n-deva", "m-deva", "ya-deva"),
    ("n_n-deva", "da-deva"),
    ("n-deva", "p_ra-deva"),
    ("n-deva", "s_tha-deva"),
    ("n-deva", "s-deva", "tta-deva"),
    ("n-deva", "s-deva", "ya-deva"),
    ("n-deva", "t_ra-deva"),
    ("n-deva", "t-deva", "sa-deva"),
    ("n-deva", "t-deva", "va-deva"),
    ("n-deva", "t-deva", "ya-deva"),
    ("n-deva", "th-deva", "va-deva"),
    ("n-deva", "th-deva", "ya-deva"),
    ("nga-deva", "k-deva", "ta-deva"),
    ("nga-deva", "kh-deva", "ya-deva"),
    ("ny-deva", "c-deva", "ya-deva"),
    ("ny-deva", "j-deva", "ya-deva"),
    ("ny-deva", "sh_ra-deva"),
    ("p-deva", "s-deva", "va-deva"),
    ("p-deva", "t-deva", "ya-deva"),
    ("ra-deva", "c-deva", "cha-deva"),
    ("s-deva", "k_ra-deva"),
    ("s-deva", "m-deva", "ya-deva"),
    ("s-deva", "n-deva", "ya-deva"),
    ("s-deva", "p-deva", "la-deva"),
    ("s-deva", "p_ra-deva"),
    ("s-deva", "t-deva", "va-deva"),
    ("s-deva", "t-deva", "ya-deva"),
    ("s-deva", "th-deva", "ya-deva"),
    ("sh_ra-deva", "ya-deva"),
    ("ss-deva", "k_ra-deva"),
    ("t-deva", "k-deva", "la-deva"),
    ("t-deva", "k_ra-deva"),
    ("t-deva", "k_ssa-deva"),
    ("t-deva", "k-deva", "ya-deva"),
    ("t-deva", "kh_na-deva"),
    ("t-deva", "kh_ra-deva"),
    ("t-deva", "m-deva", "ya-deva"),
    ("t-deva", "n-deva", "ya-deva"),
    ("t-deva", "p-deva", "la-deva"),
    ("t-deva", "p_ra-deva"),
    ("t-deva", "s-deva", "na-deva"),
    ("t-deva", "s_tha-deva"),
    ("t-deva", "s-deva", "va-deva"),
    ("t-deva", "s-deva", "ya-deva"),
    ("t-deva", "t_ra-deva"),
    ("t_t-deva", "va-deva"),
    ("tta-deva", "t_ra-deva"),
    ("v_ra-deva", "ta-deva"),
    ("b-deva", "ba-deva"),
    ("b-deva", "da-deva"),
    ("b-deva", "dha-deva"),
    ("b-deva", "ja-deva"),
    ("b-deva", "la-deva"),
    ("bh-deva", "la-deva"),
    ("bh-deva", "na-deva"),
    ("bh-deva", "va-deva"),
    ("bh-deva", "ya-deva"),
    ("c-deva", "ca-deva"),
    ("c-deva", "cha-deva"),
    ("c-deva", "da-deva"),
    ("c-deva", "dda-deva"),
    ("c-deva", "ddha-deva"),
    ("c-deva", "dha-deva"),
    ("c-deva", "ka-deva"),
    ("c-deva", "kha-deva"),
    ("c-deva", "la-deva"),
    ("c-deva", "ma-deva"),
    ("c-deva", "na-deva"),
    ("c-deva", "nna-deva"),
    ("c-deva", "pa-deva"),
    ("c-deva", "sa-deva"),
    ("c-deva", "ta-deva"),
    ("c-deva", "tha-deva"),
    ("c-deva", "tta-deva"),
    ("c-deva", "ttha-deva"),
    ("c-deva", "va-deva"),
    ("c-deva", "ya-deva"),
    ("ch-deva", "ya-deva"),
    ("dda-deva", "bha-deva"),
    ("dda-deva", "va-deva"),
    ("dh-deva", "da-deva"),
    ("dh-deva", "dha-deva"),
    ("dh-deva", "ka-deva"),
    ("dh-deva", "la-deva"),
    ("dh-deva", "na-deva"),
    ("dh-deva", "sa-deva"),
    ("dh-deva", "va-deva"),
    ("dh-deva", "ya-deva"),
    ("fa-deva", "ra-deva"),
    ("g-deva", "ba-deva"),
    ("g-deva", "bha-deva"),
    ("g-deva", "da-deva"),
    ("g-deva", "dha-deva"),
    ("g-deva", "ga-deva"),
    ("g-deva", "ja-deva"),
    ("g-deva", "ka-deva"),
    ("g-deva", "la-deva"),
    ("g-deva", "ma-deva"),
    ("g-deva", "nna-deva"),
    ("g-deva", "sa-deva"),
    ("g-deva", "ta-deva"),
    ("g-deva", "va-deva"),
    ("g-deva", "ya-deva"),
    ("gh-deva", "ba-deva"),
    ("gh-deva", "da-deva"),
    ("gh-deva", "dda-deva"),
    ("gh-deva", "gha-deva"),
    ("gh-deva", "ja-deva"),
    ("gh-deva", "la-deva"),
    ("gh-deva", "ma-deva"),
    ("gh-deva", "nna-deva"),
    ("gh-deva", "sa-deva"),
    ("gh-deva", "ta-deva"),
    ("gh-deva", "tta-deva"),
    ("gh-deva", "ttha-deva"),
    ("gh-deva", "va-deva"),
    ("gh-deva", "ya-deva"),
    ("j-deva", "ba-deva"),
    ("j-deva", "da-deva"),
    ("j-deva", "ja-deva"),
    ("j-deva", "jha-deva"),
    ("j-deva", "ka-deva"),
    ("j-deva", "la-deva"),
    ("j-deva", "ma-deva"),
    ("j-deva", "na-deva"),
    ("j-deva", "ta-deva"),
    ("j-deva", "va-deva"),
    ("j-deva", "ya-deva"),
    ("jh-deva", "ga-deva"),
    ("jh-deva", "gha-deva"),
    ("jh-deva", "jha-deva"),
    ("jh-deva", "ka-deva"),
    ("jh-deva", "la-deva"),
    ("jh-deva", "ma-deva"),
    ("jh-deva", "na-deva"),
    ("jh-deva", "ta-deva"),
    ("jh-deva", "va-deva"),
    ("jh-deva", "ya-deva"),
    ("k-deva", "ba-deva"),
    ("k-deva", "bha-deva"),
    ("k-deva", "ca-deva"),
    ("k-deva", "cha-deva"),
    ("k-deva", "da-deva"),
    ("k-deva", "dda-deva"),
    ("k-deva", "ddha-deva"),
    ("k-deva", "ga-deva"),
    ("k-deva", "ha-deva"),
    ("k-deva", "ja-deva"),
    ("k-deva", "jha-deva"),
    ("k-deva", "ka-deva"),
    ("k-deva", "kha-deva"),
    ("k-deva", "la-deva"),
    ("k-deva", "lla-deva"),
    ("k-deva", "ma-deva"),
    ("k-deva", "na-deva"),
    ("k-deva", "nna-deva"),
    ("k-deva", "pa-deva"),
    ("k-deva", "pha-deva"),
    ("k-deva", "sa-deva"),
    ("k-deva", "sha-deva"),
    ("k-deva", "ta-deva"),
    ("k-deva", "tha-deva"),
    ("k-deva", "tta-deva"),
    ("k-deva", "ttha-deva"),
    ("k-deva", "va-deva"),
    ("k-deva", "ya-deva"),
    ("kh-deva", "da-deva"),
    ("kh-deva", "kha-deva"),
    ("kh-deva", "la-deva"),
    ("kh-deva", "ma-deva"),
    ("kh-deva", "nna-deva"),
    ("kh-deva", "pa-deva"),
    ("kh-deva", "sa-deva"),
    ("kh-deva", "sha-deva"),
    ("kh-deva", "ssa-deva"),
    ("kh-deva", "ta-deva"),
    ("kh-deva", "tta-deva"),
    ("kh-deva", "ttha-deva"),
    ("kh-deva", "va-deva"),
    ("kh-deva", "ya-deva"),
    ("l-deva", "ba-deva"),
    ("l-deva", "bha-deva"),
    ("l-deva", "ca-deva"),
    ("l-deva", "da-deva"),
    ("l-deva", "dda-deva"),
    ("l-deva", "ddha-deva"),
    ("l-deva", "ga-deva"),
    ("l-deva", "ha-deva"),
    ("l-deva", "ja-deva"),
    ("l-deva", "ka-deva"),
    ("l-deva", "kha-deva"),
    ("l-deva", "la-deva"),
    ("l-deva", "ma-deva"),
    ("l-deva", "pa-deva"),
    ("l-deva", "pha-deva"),
    ("l-deva", "sa-deva"),
    ("l-deva", "ta-deva"),
    ("l-deva", "tha-deva"),
    ("l-deva", "tta-deva"),
    ("l-deva", "ttha-deva"),
    ("l-deva", "va-deva"),
    ("l-deva", "ya-deva"),
    ("ll-deva", "pa-deva"),
    ("ll-deva", "va-deva"),
    ("ll-deva", "ya-deva"),
    ("m-deva", "ba-deva"),
    ("m-deva", "bha-deva"),
    ("m-deva", "da-deva"),
    ("m-deva", "ha-deva"),
    ("m-deva", "la-deva"),
    ("m-deva", "ma-deva"),
    ("m-deva", "na-deva"),
    ("m-deva", "pa-deva"),
    ("m-deva", "sa-deva"),
    ("m-deva", "sha-deva"),
    ("m-deva", "ta-deva"),
    ("m-deva", "va-deva"),
    ("m-deva", "ya-deva"),
    ("n-deva", "ba-deva"),
    ("n-deva", "ca-deva"),
    ("n-deva", "cha-deva"),
    ("n-deva", "da-deva"),
    ("n-deva", "dda-deva"),
    ("n-deva", "ddha-deva"),
    ("n-deva", "dha-deva"),
    ("n-deva", "ga-deva"),
    ("n-deva", "ha-deva"),
    ("n-deva", "ja-deva"),
    ("n-deva", "jha-deva"),
    ("n-deva", "ka-deva"),
    ("n-deva", "kha-deva"),
    ("n-deva", "la-deva"),
    ("n-deva", "pa-deva"),
    ("n-deva", "pha-deva"),
    ("n-deva", "sa-deva"),
    ("n-deva", "sha-deva"),
    ("n-deva", "ta-deva"),
    ("n-deva", "tha-deva"),
    ("n-deva", "tta-deva"),
    ("n-deva", "ttha-deva"),
    ("n-deva", "va-deva"),
    ("n-deva", "ya-deva"),
    ("nga-deva", "ca-deva"),
    ("nga-deva", "na-deva"),
    ("nga-deva", "ya-deva"),
    ("nn-deva", "dda-deva"),
    ("nn-deva", "dddha-deva"),
    ("nn-deva", "ddha-deva"),
    ("nn-deva", "nna-deva"),
    ("nn-deva", "ta-deva"),
    ("nn-deva", "tta-deva"),
    ("nn-deva", "ttha-deva"),
    ("nn-deva", "va-deva"),
    ("nn-deva", "ya-deva"),
    ("ny-deva", "cha-deva"),
    ("ny-deva", "sha-deva"),
    ("p-deva", "da-deva"),
    ("p-deva", "dda-deva"),
    ("p-deva", "ddha-deva"),
    ("p-deva", "dha-deva"),
    ("p-deva", "ka-deva"),
    ("p-deva", "la-deva"),
    ("p-deva", "lla-deva"),
    ("p-deva", "ma-deva"),
    ("p-deva", "na-deva"),
    ("p-deva", "nna-deva"),
    ("p-deva", "pa-deva"),
    ("p-deva", "pha-deva"),
    ("p-deva", "sa-deva"),
    ("p-deva", "ssa-deva"),
    ("p-deva", "ta-deva"),
    ("p-deva", "tha-deva"),
    ("p-deva", "ttha-deva"),
    ("p-deva", "va-deva"),
    ("p-deva", "ya-deva"),
    ("ph-deva", "da-deva"),
    ("ph-deva", "ja-deva"),
    ("ph-deva", "ka-deva"),
    ("ph-deva", "la-deva"),
    ("ph-deva", "ma-deva"),
    ("ph-deva", "na-deva"),
    ("ph-deva", "pha-deva"),
    ("ph-deva", "sha-deva"),
    ("ph-deva", "ta-deva"),
    ("ph-deva", "tta-deva"),
    ("ph-deva", "ya-deva"),
    ("s-deva", "ba-deva"),
    ("s-deva", "cha-deva"),
    ("s-deva", "da-deva"),
    ("s-deva", "dda-deva"),
    ("s-deva", "ddha-deva"),
    ("s-deva", "ja-deva"),
    ("s-deva", "ka-deva"),
    ("s-deva", "kha-deva"),
    ("s-deva", "la-deva"),
    ("s-deva", "ma-deva"),
    ("s-deva", "na-deva"),
    ("s-deva", "pa-deva"),
    ("s-deva", "pha-deva"),
    ("s-deva", "sa-deva"),
    ("s-deva", "ta-deva"),
    ("s-deva", "tta-deva"),
    ("s-deva", "ttha-deva"),
    ("s-deva", "va-deva"),
    ("s-deva", "ya-deva"),
    ("sh-deva", "ba-deva"),
    ("sh-deva", "cha-deva"),
    ("sh-deva", "ka-deva"),
    ("sh-deva", "kha-deva"),
    ("sh-deva", "la-deva"),
    ("sh-deva", "ma-deva"),
    ("sh-deva", "sha-deva"),
    ("sh-deva", "ta-deva"),
    ("sh-deva", "tta-deva"),
    ("sh-deva", "ya-deva"),
    ("ss-deva", "ka-deva"),
    ("ss-deva", "ma-deva"),
    ("ss-deva", "nna-deva"),
    ("ss-deva", "pa-deva"),
    ("ss-deva", "va-deva"),
    ("t-deva", "ba-deva"),
    ("t-deva", "bha-deva"),
    ("t-deva", "ka-deva"),
    ("t-deva", "kha-deva"),
    ("t-deva", "la-deva"),
    ("t-deva", "ma-deva"),
    ("t-deva", "na-deva"),
    ("t-deva", "pa-deva"),
    ("t-deva", "pha-deva"),
    ("t-deva", "sa-deva"),
    ("t-deva", "tha-deva"),
    ("t-deva", "va-deva"),
    ("t-deva", "ya-deva"),
    ("th-deva", "ka-deva"),
    ("th-deva", "la-deva"),
    ("th-deva", "ma-deva"),
    ("th-deva", "sa-deva"),
    ("th-deva", "tha-deva"),
    ("th-deva", "va-deva"),
    ("th-deva", "ya-deva"),
    ("v-deva", "ha-deva"),
    ("v-deva", "la-deva"),
    ("v-deva", "na-deva"),
    ("v-deva", "sa-deva"),
    ("v-deva", "ya-deva"),
    ("y-deva", "ya-deva"),
]

iiMatraPres = [
    "fa-deva",
    "f_ra-deva",
    "jha-deva.loclNEP",
    "ka-deva",
    "k_va-deva",
    "k_ra-deva",
    "k_ra-deva.alt",
    "k_ka-deva",
    "k_la-deva.loclMAR",
    "k_ta-deva",
    "k_t_ta-deva",
    "pha-deva",
    "ph_ra-deva",
    "ph_la-deva.loclMAR",
    "qa-deva",
    "ra_uuMatra-deva",
    "zha-deva.loclNEP",
    "rVocalic-deva",
    "rrVocalic-deva",
]


def createClass(font, myClassName, listOfGlyphNames):
    listOfClasses = font.classes
    listOfClassNames = [c.name for c in listOfClasses]

    myClassCode = " ".join(listOfGlyphNames)

    if myClassName in listOfClassNames:
        # print "Changing class", myClassName, "to these glyphs:", myClassCode
        font.classes[str(myClassName)].code = myClassCode

    else:
        # print "Creating class", myClassName, "with these glyphs:", myClassCode
        myNewClass = GSClass()
        myNewClass.name = myClassName
        myNewClass.code = myClassCode
        font.classes.append(myNewClass)


def updated_code(oldcode, beginsig, endsig, newcode):
    """Replaces text in oldcode with newcode, but only between beginsig and endsig."""
    begin_offset = oldcode.find(beginsig)
    end_offset = oldcode.find(endsig) + len(endsig)
    newcode = (
        oldcode[:begin_offset]
        + beginsig
        + newcode
        + "\n"
        + endsig
        + oldcode[end_offset:]
    )
    return newcode


def create_otfeature(
    featurename="temp",
    featurecode="# empty feature code",
    targetfont=font,
    codesig="DEFAULT-CODE-SIGNATURE",
):
    """
    Creates or updates an OpenType feature in the font.
    Returns a status message in form of a string.
    """

    beginSig = "# BEGIN " + codesig + "\n"
    endSig = "# END " + codesig + "\n"

    if featurename in [f.name for f in targetfont.features]:
        # feature already exists:
        targetfeature = targetfont.features[featurename]

        if beginSig in targetfeature.code:
            # replace old code with new code:
            targetfeature.code = updated_code(
                targetfeature.code, beginSig, endSig, featurecode
            )
        else:
            # append new code:
            targetfeature.code += "\n" + beginSig + featurecode + "\n" + endSig

        return "Updated existing OT feature '%s'." % featurename
    else:
        # create feature with new code:
        newFeature = GSFeature()
        newFeature.name = featurename
        newFeature.code = beginSig + featurecode + "\n" + endSig
        targetfont.features.append(newFeature)
        return "Created new OT feature '%s'" % featurename


def create_prefix(
    featurename="temp",
    featurecode="# empty feature code",
    targetfont=font,
    codesig="DEFAULT-CODE-SIGNATURE",
):
    """
    Creates or updates an OpenType prefix in the font.
    Returns a status message in form of a string.
    """

    beginSig = "# BEGIN " + codesig + "\n"
    endSig = "# END " + codesig + "\n"
    prefixes = targetfont.featurePrefixes
    pre2 = []
    for x in range(0, len(prefixes)):
        pre2.append(prefixes[x])

    if featurename in [f.name for f in pre2]:
        # feature already exists:
        targetfeature = targetfont.featurePrefixes[featurename]

        if beginSig in targetfeature.code:
            # replace old code with new code:
            targetfeature.code = updated_code(
                targetfeature.code, beginSig, endSig, featurecode
            )
        else:
            # append new code:
            targetfeature.code += "\n" + beginSig + featurecode + "\n" + endSig

        return "Updated existing OT prefix '%s'." % featurename
    else:
        # create feature with new code:
        newFeature = GSFeaturePrefix()
        newFeature.name = featurename
        newFeature.code = beginSig + featurecode + "\n" + endSig
        targetfont.featurePrefixes.append(newFeature)
        return "Created new OT prefix '%s'" % featurename


def listDevanagari(font):
    list = []
    for glyph in font.glyphs:
        if glyph.category == "Letter" and glyph.script == "devanagari":
            list.append(glyph.name)
    return list


def listHalfforms(font):
    list = []
    for glyph in font.glyphs:
        if glyph.category == "Letter" and glyph.script == "devanagari":
            if glyph.subCategory == "Halfform":
                list.append(glyph.name)
    return list


def listFullforms(font):
    list = []
    for glyph in font.glyphs:
        if glyph.category == "Letter" and glyph.script == "devanagari":
            if glyph.subCategory == "Other":
                list.append(glyph.name)
    return list


def listConjuncts(font):
    list = []
    for glyph in font.glyphs:
        if glyph.category == "Letter" and glyph.script == "devanagari":
            if glyph.subCategory == "Ligature":
                list.append(glyph.name)
    return list


def listiMatraBase(font):
    list = ["iMatra-deva"]
    for glyph in font.glyphs:
        if glyph.name.startswith("iMatra_") and glyph.name.find(".") < 0:
            list.append(glyph.name)
    return list


def listBegin(font, string):
    list = []
    for glyph in font.glyphs:
        if glyph.name.startswith(string):
            list.append(glyph.name)
    return list


# chequea que todos los glifos existan
def checkExistence(font, list):
    existence = True
    for item in list:
        if font.glyphs[item]:
            a = 0
        else:
            existence = False
    return existence


# suma de anchos
def widthSum(font, list):
    ancho = 0
    for item in list:
        ancho += font.glyphs[item].layers[0].width
    # ajusta el ultimo signo al anchor, elimina ultimo width y agrega top.x
    if font.glyphs[item].layers[0].anchors["top"]:
        ancho = (
            ancho
            - font.glyphs[item].layers[0].width
            + font.glyphs[item].layers[0].anchors["top"].x
        )
    return ancho


def findIMatra(font, width, list):
    differences = []
    for iMatra in list:
        iwidth = (font.glyphs[iMatra].layers[0].anchors["imatra"].x) - (
            font.glyphs[iMatra].layers[0].width
        )
        differences.append(abs(iwidth - width))

    index = differences.index(min(differences))
    return list[index]


def getiMatraGlyphs(iMatra, list):
    glyphs = []
    # string=''
    for item in list:
        if item[0] == iMatra:
            glyphs.append(item[1])
    return glyphs


def iMatraGlyphs(font, list, measure):
    iMatrasGlyphs = []
    iMatrasList = listBegin(font, "iMatra-deva.")
    for glyphname in list:
        layer = font.glyphs[glyphname].layers[0]
        if measure == "top":
            if layer.anchors["top"]:
                width = layer.anchors["top"].x
            else:
                print(layer.parent.name + " no tiene anchor top")
                width = layer.width
        else:
            width = layer.width

        iMatra = findIMatra(font, width, iMatrasList)
        iMatrasGlyphs.append([iMatra, glyphname, width])

    classes = []
    for item in iMatrasList:
        glyphs = getiMatraGlyphs(item, iMatrasGlyphs)
        if len(glyphs) > 0:
            classes.append([item, glyphs])
    return classes


def createWidthClasses(font):
    half = iMatraGlyphs(font, listHalfforms(font), "width")

    for iMatra in half:
        createClass(font, "DevaHalf" + iMatra[0][-3:], iMatra[1])
    # full=iMatraGlyphs(font,listFullforms(font),'top')
    full = iMatraGlyphs(font, listFullforms(font) + listConjuncts(font), "top")
    for iMatra in full:
        createClass(font, "DevaFull" + iMatra[0][-3:], iMatra[1])
    return half, full


def digit(num):
    if len(num) > 1 and num[0] == "0":
        num = num[1]
    return int(num)


def feature_pres(font, presList):
    code1 = "#Widths by classes\n"
    # primera parte, grupos por ancho
    iMatrasList = listBegin(font, "iMatra-deva.")
    listOfClasses = font.classes
    listOfClassNames = [c.name for c in listOfClasses]
    for c in listOfClassNames:
        if c.startswith("DevaFull."):
            pos = len(c) - c.find(".")
            suffix = c[-pos:]
            code1 += (
                "sub [@iMatraBase]' [@"
                + c
                + "] by [iMatra-deva"
                + suffix
                + " iMatra_reph-deva"
                + suffix
                + " iMatra_reph_anusvara-deva"
                + suffix
                + "];\n"
            )

    # segunda parte: combinaciones de anchos

    widths = []
    for im in iMatrasList:
        widths.append(
            (font.glyphs[im].layers[0].anchors["imatra"].x)
            - (font.glyphs[im].layers[0].width)
        )
    devaHalfClasses = []
    devaFullClasses = []

    for c in listOfClassNames:
        if c.startswith("DevaHalf."):
            devaHalfClasses.append(c)
        elif c.startswith("DevaFull."):
            devaFullClasses.append(c)

    # triple combinacion
    code2 = "#Triple combinations\n"
    for c1 in devaHalfClasses:
        for c2 in devaHalfClasses:
            for c3 in devaFullClasses:
                # calculo de ancho
                # obtengo el numero de clase y lo convierto a indice
                val1 = digit(c1[-2:])
                val2 = digit(c2[-2:])
                val3 = digit(c3[-2:])
                im1width = widths[val1]
                im2width = widths[val2]
                im3width = widths[val3]
                suma = widths[val1] + widths[val2] + widths[val3]
                replace = findIMatra(font, suma, iMatrasList)
                suffix = replace[-pos:]
                code2 += (
                    "sub [@iMatraBase]' [@"
                    + c1
                    + "] [@"
                    + c2
                    + "] [@"
                    + c3
                    + "] by ["
                    + replace
                    + " iMatra_reph-deva"
                    + suffix
                    + " iMatra_reph_anusvara-deva"
                    + suffix
                    + "];\n"
                )

    # doble combinacion
    code2 += "#Double combinations\n"
    for c1 in devaHalfClasses:

        for c2 in devaFullClasses:
            # calculo de ancho
            val1 = digit(c1[-2:])
            val2 = digit(c2[-2:])
            suma = widths[val1] + widths[val2]
            replace = findIMatra(font, suma, iMatrasList)
            suffix = replace[-pos:]
            code2 += (
                "sub [@iMatraBase]' [@"
                + c1
                + "] [@"
                + c2
                + "] by ["
                + replace
                + " iMatra_reph-deva"
                + suffix
                + " iMatra_reph_anusvara-deva"
                + suffix
                + "];\n"
            )

    # tercera parte: combinaciones predeclaradas
    code3 = "#Predefined combinations\n"
    for item in presList:
        if checkExistence(font, item) and len(item) > 2:
            width = widthSum(font, item)
            iMatra = findIMatra(font, width, iMatrasList)
            suffix = iMatra[-3:]
            glyphList = " ".join(item)
            code3 += (
                "sub [@iMatraBase]' "
                + glyphList
                + " by [iMatra-deva"
                + suffix
                + " iMatra_reph-deva"
                + suffix
                + " iMatra_reph_anusvara-deva"
                + suffix
                + "];\n"
            )

    # cuarta parte: iiMatra
    code4 = ""
    if checkExistence(
        font,
        [
            "iiMatra-deva",
            "iiMatra_reph-deva",
            "iiMatra_reph_anusvara-deva",
            "iiMatra-deva.01",
        ],
    ):
        code4 = "#iMatra substitution\n"
        code4 += "sub ["
        for item in iiMatraPres:
            if font.glyphs[item]:
                code4 += item + " "
        code4 += "] [iiMatra-deva iiMatra_reph-deva iiMatra_reph_anusvara-deva]' by [iiMatra-deva.01 iiMatra_reph-deva.01 iiMatra_reph_anusvara-deva.01];"

    create_otfeature(
        featurename="pres",
        featurecode=code3 + code2 + code1 + code4,
        codesig="Pre-Base Substitutions",
        targetfont=font,
    )

    return code3 + code2 + code1 + code4


def feature_abvs(font):
    code = ""
    base = ["reph-deva", "anusvara-deva", "reph_anusvara-deva"]
    if checkExistence(
        font, base + ["iMatra-deva", "iMatra_reph-deva", "iMatra_reph_anusvara-deva"]
    ):
        code += """sub iMatra-deva reph-deva anusvara-deva by iMatra_reph_anusvara-deva;
		sub iMatra-deva reph-deva by iMatra_reph-deva;
"""
    if checkExistence(
        font, base + ["iiMatra-deva", "iiMatra_reph-deva", "iiMatra_reph_anusvara-deva"]
    ):
        code += """sub iiMatra-deva reph-deva anusvara-deva by iiMatra_reph_anusvara-deva;
sub iiMatra-deva reph-deva by iiMatra_reph-deva;
"""
    if checkExistence(
        font,
        base
        + [
            "oMatra-deva",
            "oMatra_reph-deva",
            "oMatra_anusvara-deva",
            "oMatra_reph_anusvara-deva",
        ],
    ):
        code += """sub oMatra_anusvara-deva reph-deva by oMatra_reph_anusvara-deva;
sub oMatra-deva anusvara-deva by oMatra_anusvara-deva;
sub oMatra-deva reph-deva by oMatra_reph-deva;

"""
    if checkExistence(
        font,
        base
        + [
            "auMatra-deva",
            "auMatra_anusvara-deva",
            "auMatra_reph-deva",
            "auMatra_reph_anusvara-deva",
        ],
    ):
        code += """sub auMatra-deva anusvara-deva by auMatra_anusvara-deva;
sub auMatra-deva reph-deva by auMatra_reph-deva;
sub auMatra_anusvara-deva reph-deva by auMatra_reph_anusvara-deva;
"""
    if checkExistence(
        font,
        base
        + [
            "eMatra-deva",
            "eMatra_anusvara-deva",
            "eMatra_reph-deva",
            "eMatra_reph_anusvara-deva",
        ],
    ):
        code += """sub eMatra-deva anusvara-deva by eMatra_anusvara-deva;
sub eMatra-deva reph-deva by eMatra_reph-deva;
sub eMatra_anusvara-deva reph-deva by eMatra_reph_anusvara-deva;
"""
    if checkExistence(
        font,
        base
        + [
            "aiMatra-deva",
            "aiMatra_anusvara-deva",
            "aiMatra_reph-deva",
            "aiMatra_reph_anusvara-deva",
        ],
    ):
        code += """sub aiMatra-deva anusvara-deva by aiMatra_anusvara-deva;
sub aiMatra-deva reph-deva by aiMatra_reph-deva;
sub aiMatra_anusvara-deva reph-deva by aiMatra_reph_anusvara-deva;
"""
    if checkExistence(
        font,
        base
        + [
            "rakar-deva",
            "uMatra-deva",
            "uuMatra-deva",
            "rakar_uMatra-deva",
            "rakar_uuMatra-deva",
        ],
    ):
        code += """sub reph-deva anusvara-deva by reph_anusvara-deva;
sub rakar-deva uMatra-deva by rakar_uMatra-deva;
sub rakar-deva uuMatra-deva by rakar_uuMatra-deva;
"""
    if checkExistence(font, base):
        code += """

sub @iMatra' @Deva [reph-deva] by @iMatra_reph;
sub @iMatra' @Deva [reph_anusvara-deva] by @iMatra_reph_anusvara;
sub @iMatra' @Deva @Deva [reph-deva] by @iMatra_reph;
sub @iMatra' @Deva @Deva [reph_anusvara-deva] by @iMatra_reph_anusvara;
sub @iMatra' @Deva @Deva @Deva [reph-deva] by @iMatra_reph;
sub @iMatra' @Deva @Deva @Deva [reph_anusvara-deva] by @iMatra_reph_anusvara;
sub @iMatra' @Deva @Deva @Deva @Deva [reph-deva] by @iMatra_reph;
sub @iMatra' @Deva @Deva @Deva @Deva [reph_anusvara-deva] by @iMatra_reph_anusvara;
"""
    if checkExistence(font, base):
        code += """
#remove reph
sub [@iMatra_reph @iMatra_reph_anusvara] @Deva' lookup removeReph [reph-deva reph_anusvara-deva]';
sub [@iMatra_reph @iMatra_reph_anusvara] @Deva @Deva' lookup removeReph [reph-deva reph_anusvara-deva]';
sub [@iMatra_reph @iMatra_reph_anusvara] @Deva @Deva @Deva' lookup removeReph [reph-deva reph_anusvara-deva]';
sub [@iMatra_reph @iMatra_reph_anusvara] @Deva @Deva @Deva @Deva' lookup removeReph [reph-deva reph_anusvara-deva]';
sub [@iMatra_reph @iMatra_reph_anusvara] @Deva @Deva @Deva @Deva @Deva' lookup removeReph [reph-deva reph_anusvara-deva]';
"""
    if checkExistence(
        font,
        base
        + [
            "candraBindu-deva",
            "candraBindu-deva.alt",
            "anusvara-deva",
            "anusvara-deva.alt",
        ],
    ):
        code += """#utiliza un candraBindu alternativo en iMatra
sub [@iMatra @iMatra_reph @iMatra_reph_anusvara] @Deva candraBindu-deva' by candraBindu-deva.alt;
sub [@iMatra @iMatra_reph @iMatra_reph_anusvara] @Deva @Deva candraBindu-deva' by candraBindu-deva.alt;
sub [@iMatra @iMatra_reph @iMatra_reph_anusvara] @Deva @Deva @Deva candraBindu-deva' by candraBindu-deva.alt;
sub [@iMatra @iMatra_reph @iMatra_reph_anusvara] @Deva @Deva @Deva @Deva candraBindu-deva' by candraBindu-deva.alt;

#utiliza un anusvara alternativo en iMatra
sub [@iMatra @iMatra_reph @iMatra_reph_anusvara] @Deva anusvara-deva' by anusvara-deva.alt;
sub [@iMatra @iMatra_reph @iMatra_reph_anusvara] @Deva @Deva anusvara-deva' by anusvara-deva.alt;
sub [@iMatra @iMatra_reph @iMatra_reph_anusvara] @Deva @Deva @Deva anusvara-deva' by anusvara-deva.alt;
sub [@iMatra @iMatra_reph @iMatra_reph_anusvara] @Deva @Deva @Deva @Deva anusvara-deva' by anusvara-deva.alt;

#candraBindu y anusvara alternativo despues de reph
sub [reph-deva reph_anusvara-deva] [candraBindu-deva anusvara-deva]' by [candraBindu-deva.alt anusvara-deva.alt];
"""

    create_otfeature(
        featurename="abvs",
        featurecode=code,
        codesig="Above-Base Substitutions",
        targetfont=font,
    )


def DevaRemoveReph(font, list):
    code = "lookup removeReph {\n"
    for glyph in list:
        code += "sub " + glyph + " [reph-deva reph_anusvara-deva] by " + glyph + ";\n"
    code += "} removeReph;"

    create_prefix("DevaRemoveReph", code, font, "removeReph")
    return code


font.disableUpdateInterface()

if classes == True:
    createClass(font, "DevaHalfforms", listHalfforms(font))
    createClass(font, "DevaFullforms", listFullforms(font))
    createClass(font, "DevaCjct", listConjuncts(font))
    createClass(
        font, "Deva", listFullforms(font) + listHalfforms(font) + listConjuncts(font)
    )
    createClass(font, "iMatraBase", listiMatraBase(font))
    createClass(font, "iMatra", listBegin(font, "iMatra-deva"))
    createClass(font, "iMatra_reph", listBegin(font, "iMatra_reph-deva"))
    createClass(
        font, "iMatra_reph_anusvara", listBegin(font, "iMatra_reph_anusvara-deva")
    )
    createWidthClasses(font)
if features == True:
    feature_pres(font, presList)
    feature_abvs(font)

if prefix == True:
    DevaRemoveReph(
        font, listFullforms(font) + listHalfforms(font) + listConjuncts(font)
    )

font.enableUpdateInterface()
