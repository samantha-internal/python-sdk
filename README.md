# Whitehead SDK

## Installation and usage

### Build

`poetry install`

`poetry run codegen`

`poetry build`

### Install

`pip install whitehead_sdk`

## API list

### answer

Given a question and a context, generates the answer to the question

```python
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
result = client.answer("What color is the apple?", "The apple is red")
assert result == "red"
```

### chitchat

Given a phrase and a list of history messages, generates the corresponding bot response

```python
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
result = client.chitchat(
    "good bye", [{"bot": "hi"}, {"user": "hello"}, {"bot": "howdy?"}]
)
assert result == "bye"
```

### choose

Given a question, a context and a list of choices, returns the most likely choice from the list

```python
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
result = client.choose("What color is the apple?", "The apple is red", ["big", "red", "blue"])
assert result == "red"
```

### dialogact

Given a phrase, returns a type of dialog act type for it.

```python
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
result = client.dialogact("hi there")
assert result == "Conventional-opening"
```

### paraphrase

Given a phrase, returns a list of paraphrases

```python
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
result = client.paraphrase("I like pizza")
assert set(result) == {
    "I like pizza.",
    "I enjoy pizza.",
    "I like to eat pizza.",
    "I like eating pizza.",
    "I like food.",
    "I love pizza.",
}
```

### relations

Given a word/phrase and a relation type, returns a list of related words/phrases, according to the relation type 

```python
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
result = client.relations("pizza", Relation.IsA)
assert set(result) == {
    "food",
    "pizza",
    "fast food",
    "italian food",
    "usually",
    "popular food",
    "often",
    "meal",
    "sometimes",
    "cook",
}
```

### sensibility

Given a list of phrases and a history, ranks them according to how sensible they are in a given history context

```python
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
result = client.sensibility(
    ["fine", "bye"], [{"user": "hi"}, {"bot": "hi there"}, {"user": "howdy?"}]
)
alts = {a["alternative"] for a in result}
scores = [a["score"] for a in result]
assert len(alts) == 2
assert alts == {"fine", "bye"}
assert all([isinstance(s, float) for s in scores])
```

### sentiment

Given a phrase, returns a sentiment information represented as a floating point value

```python
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
result = client.sentiment("I feel good")
assert len(result) == 1
assert result[0]["label"] == "positive"
assert result[0]["score"] >= 0.9
```

### similarity

Given a target sentence and a list of other sentences, returns an array of pairwise similarity scores

```python
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
result = client.similarity(
    "I want pizza",
    ["I would like to have a pie", "I don't want pizza", "I want taco"],
)
assert len(result) == 3
assert result[0]["candidate"] == "I would like to have a pie"
assert result[0]["score"] >= 0.9
assert result[1]["candidate"] == "I don't want pizza"
assert result[1]["score"] <= 0.5
assert result[2]["candidate"] == "I want taco"
assert result[2]["score"] <= 0.5
```

### speak

Converts phrase to audio

```python
import io
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
stream = io.BytesIO()
# stream could be an open file as well
client.speak("hi", stream)
```

### topics

Given a phrase and a list of topics, returns how likely is each topic to be the good fit for the phrase

```python
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
result = client.topics("hi", allow_multiple=True, topics=["greeting", "food"])
assert len(result) == 2
assert result[0]["topic"] == "greeting"
assert result[0]["score"] >= 0.5
assert result[1]["topic"] == "food"
assert result[1]["score"] <= 0.5
```

### transcribe

Converts audio to text

```python
import io
from whitehead_sdk import authenticate


developer_id = <int> # Check your profile on the dashboard for this.
api_key = "<64 letter api key available on your whitehead dashboard>"
client = authenticate(api_key, developer_id)
stream = io.BytesIO()
# ... write audio bytes to the stream ...
# it could be an open file as well
result = client.transcribe(stream)
assert isinstance(result, str)
```
