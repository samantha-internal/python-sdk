import io, os, sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from gql.transport.exceptions import TransportQueryError
from whitehead_sdk import authenticate
from whitehead_sdk.api.input.turn import Turn
from whitehead_sdk.api.enum.relation import Relation


@pytest.fixture(scope="module")
def client():
    return authenticate(
        os.environ["WHITEHEAD_API_KEY"], int(os.environ["WHITEHEAD_DEVELOPER_ID"])
    )


def test_answer(client):
    result = client.answer("What color is the apple?", "The apple is red")
    assert result == "red"


def test_chitchat(client):
    result = client.chitchat(
        "good bye", [{"bot": "hi"}, {"user": "hello"}, {"bot": "howdy?"}]
    )
    assert result == "bye"


def test_chitchat_missing_bot_turn(client):
    try:
        client.chitchat("good bye", [{"bot": "hi"}, {"user": "hello"}])
    except TransportQueryError:
        assert True
    except Exception:
        assert False
    else:
        assert False


def test_choose(client):
    result = client.choose("What color is the apple?", "The apple is red", ["big", "red", "blue"])
    assert result == "red"


def test_dialogact(client):
    result = client.dialogact("hi there")
    assert result == "Conventional-opening"


def test_paraphrase(client):
    result = client.paraphrase("I like pizza")
    assert set(result) == {
        "I like pizza.",
        "I enjoy pizza.",
        "I like to eat pizza.",
        "I like eating pizza.",
        "I like food.",
        "I love pizza.",
    }


def test_relations(client):
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


def test_sensibility(client):
    result = client.sensibility(
        ["fine", "bye"], [{"user": "hi"}, {"bot": "hi there"}, {"user": "howdy?"}]
    )
    alts = {a["alternative"] for a in result}
    scores = [a["score"] for a in result]
    assert len(alts) == 2
    assert alts == {"fine", "bye"}
    assert all([isinstance(s, float) for s in scores])


def test_sentiment(client):
    result = client.sentiment("I feel good")
    assert len(result) == 1
    assert result[0]["label"] == "positive"
    assert result[0]["score"] >= 0.9


def test_similarity(client):
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


def test_speak_and_transcribe(client):
    stream = io.BytesIO()
    client.speak("hi", stream)
    stream.seek(0)
    result = client.transcribe(stream)
    assert result in ("I",)


def test_topics(client):
    result = client.topics("hi", allow_multiple=True, topics=["greeting", "food"])
    assert len(result) == 2
    assert result[0]["topic"] == "greeting"
    assert result[0]["score"] >= 0.5
    assert result[1]["topic"] == "food"
    assert result[1]["score"] <= 0.5
