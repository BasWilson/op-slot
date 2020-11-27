def stringToJsonError(errorString, errorData={}):
    return {
        "error": errorString,
        "errorData": errorData
    }
