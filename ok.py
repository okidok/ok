questionList = {
      q1: "is it bigger than a bread box?",
      q2: "is it alive?",
      q3: "is it an animal?",
      q4: "is it a plant?",
      q5: "is it from a movie?",
      q6: "is it smaller than a bread box?",
      q7: "is it electronic",
      q8: "is it grown in a garden?",
      q9: "is it a human?",
      q10: "is it food?",
      q11: "is it a book?",
      q12: "are they male or female",
      q13: "is it man made?",
      q14: "do they have glasses?"
      q15: "does it have metal in it?",
      q16: "would it be found in a house?",
      q17: "does it live in the wild?",
      q18: "is it a pet?",
      q19: "does it wear pants?",
      q20: "is it wearable?",
      q21: "are they a wizard",
      q22: "are they from a comic book?",
      q23:"does it kill people?",
      q24:"does it go bang?",
      q25: "is it a weapon?"
      q26: "is it used to store bread?",
      q27: "is it a container?",



}
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.sql import text



engine = create_engine('sqlite:///:memory:', echo=True)

def main():
  conn = engine.connect()
  metadata = MetaData()
  createTables(metadata, conn)
  s = text("SELECT users.fullname AS title FROM users")
  statement = text("INSERT INTO users (name, fullname) values ('hal', 'Halsted Matthew Larsson')")
  conn.execute(statement)

  query = text("Select * from users")
  result = conn.execute(query).fetchall()
  print(result)






def createTables(metadata, conn):
  users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String))

  metadata.create_all(engine)

answerList = [
    "dog",
    "flower",
    "sandwich",
    "Harry Potter",
    "chips",
    "laptop",
    "phone",
    "gun",
    "Batman",
    "tiger",
    "pineapple",
    "tree",
    "bread box",

]

def main():
  print ("Ask yes or no questions, try to stay simple, capitalize names, and don't get too specific")
  printHeader()
  selection = getUserSelection()
  print(getQuestionAnswer(selection, questionList, answerList))

def getUserSelection():
  while(True):
      answer =  input("Type question and press enter")
      if answer in inputQuestions:
          return answer
      else:
          print "question not recognized."

#code by Hal
def getQuestionAnswer(question, questionList, answerList):
    index = questionList.index(question)
    answer = answerList[index]
    return answer

main()
