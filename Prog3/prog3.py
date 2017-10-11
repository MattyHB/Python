import lmc
import bottle



@bottle.route('/')
 def hello():
     return Demo_HTML

 
 
 
 # Launch the BottlePy dev server
 if __name__== "__main__":
    bottle.run(host='localhost', debug=True)


Demo_HTML = '''
<html>

<body>
    <h1>Little Man Computer</h1>
    <form>
        <pre> 0[800]  1[308]  2[800]  3[108]  4[900]  5[0  ]  6[123]  7[0  ]  8[2  ]  9[0  ] 
10[0  ] 11[0  ] 12[0  ] 13[0  ] 14[0  ] 15[0  ] 16[0  ] 17[0  ] 18[0  ] 19[0  ] 
20[0  ] 21[0  ] 22[0  ] 23[0  ] 24[0  ] 25[0  ] 26[0  ] 27[0  ] 28[0  ] 29[0  ] 
30[0  ] 31[0  ] 32[0  ] 33[0  ] 34[0  ] 35[0  ] 36[0  ] 37[0  ] 38[0  ] 39[0  ] 
40[0  ] 41[0  ] 42[0  ] 43[0  ] 44[0  ] 45[0  ] 46[0  ] 47[0  ] 48[0  ] 49[0  ] 
50[0  ] 51[0  ] 52[0  ] 53[0  ] 54[0  ] 55[0  ] 56[0  ] 57[0  ] 58[0  ] 59[0  ] 
60[0  ] 61[0  ] 62[0  ] 63[0  ] 64[0  ] 65[0  ] 66[0  ] 67[0  ] 68[0  ] 69[0  ] 
70[0  ] 71[0  ] 72[0  ] 73[0  ] 74[0  ] 75[0  ] 76[0  ] 77[0  ] 78[0  ] 79[0  ] 
80[0  ] 81[0  ] 82[0  ] 83[0  ] 84[0  ] 85[0  ] 86[0  ] 87[0  ] 88[0  ] 89[0  ] 
90[0  ] 91[0  ] 92[0  ] 93[0  ] 94[0  ] 95[0  ] 96[0  ] 97[0  ] 98[0  ] 99[0  ] 
                                PC[5 ] Acc[11 ] HLT
In box: [4]
Out box:[11]
        </pre>
        <input type="submit" name="action" value="Step">
        <input type="submit" name="action" value="Run">
        <h2>Load Program</h2>
        <textarea name="program" rows="20" cols="30">Enter program here</textarea><br>
        Enter input here (comma-delimited numbers): <input type="text" name="inbox" value="2,3,4">
        <input type="submit" name="action" value="Load">
    </form>
</body>

</html>''' 