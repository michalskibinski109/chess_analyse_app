
![example workflow](https://github.com/michalskibinski109/chess_analyse_app/actions/workflows/python-app.yml/badge.svg)
# chess_analyse_app
! project still under development

### how does it work
1. send get request to chess.com api with given username to get all of the player games
2. convert png strings to python objects
3. convert python objects to dataframe
4. shows all of information about games on charts using django web app. (TODO)

### example convert module output:
```
games played on chess.com: 268
games played on lichess: 0
example game:
  time_control: 60+0
    player:   
      color: Color.White
      elo: 1459
    opponent:
      color: Color.Black
      elo: 1327
result: Result.Black
date: 2018-09-28 18:10:30
```


