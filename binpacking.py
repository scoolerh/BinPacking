import flask
import json

app = flask.Flask(__name__)

binsList = []

@app.route('/')
def home():
    return "hi"

@app.route('/newproblem/')
def newproblem():
    id = len(binsList)
    binEncoding = "##"
    binsList.append(binEncoding)
    newproblem = {'ID': id, 'bins': binEncoding}
    return newproblem

@app.route('/placeitem/<problemID>/<size>')
def placeitem(problemID, size):
    problem = binsList[int(problemID)]
    size = int(size)
    bins = problem[2:-1].split('#')
    added = False
    for i in range(len(bins)):
        sizeList = bins[i].split('!')
        if (sizeList[0] == ''): 
            bins[i] = str(size)
            added = True
            break
        spaceTaken = 0
        for item in sizeList: 
            spaceTaken += int(item)
        if (spaceTaken + size <= 100): 
            bins[i] += '!' + str(size)
            added = True
            break
    if (added == False): 
        bins.append(str(size))
    final = '##'
    for bin in bins: 
        final += bin + '#'
    #final += '' if len(bins) == 0 else '#'
    binsList[int(problemID)] = final
    return final + "#"

if __name__ == '__main__': 
    host = 'localhost'
    port = 5001
    app.run(host=host, port=port, debug=True)