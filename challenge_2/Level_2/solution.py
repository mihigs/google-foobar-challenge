def solution(l):
    return parseStrings(l);

def parseStrings(l):
    maxLength = 0;
    versionsList = [];

    for tag in l:
        version = tag.split('.');
        versionsList.append(version);

        if len(version) > maxLength:
            maxLength = len(version);

    return startSort(generateMatrix(versionsList, maxLength), maxLength);

def generateMatrix(l, maxLength):
    matrix = l;
    for element in matrix:
        element.extend([-1] * (maxLength - len(element)));
    return matrix;

def startSort(versions, maxLength):
    layer = maxLength - 1;
    result = [];

    while layer >= 0:
        versions.sort(key=lambda x: int(x[layer]));
        layer -= 1;    

    for version in versions:
        while -1 in version: version.remove(-1)
        result.append(".".join(version));

    return result;


