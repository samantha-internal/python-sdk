from typing import List, Optional
from gql.client import Client
from .api.answer import answer as _answer
from .api.chitchat import chitchat as _chitchat
from .api.choose import choose as _choose
from .api.dialogact import dialogact as _dialogact
from .api.paraphrase import paraphrase as _paraphrase
from .api.relations import relations as _relations
from .api.sensibility import sensibility as _sensibility
from .api.sentiment import sentiment as _sentiment
from .api.similarity import similarity as _similarity
from .api.speak import speak as _speak
from .api.topics import topics as _topics
from .api.transcribe import transcribe as _transcribe
from .api.input.turn import Turn
from .api.enum.relation import Relation

class GraphqlClient(Client):
    def answer(self, input: str, context: str) -> _answer.answerData.AnswerResult: ...
    def chitchat(
        self, input: str, history: List[Turn] = []
    ) -> _chitchat.chitchatData.ChitchatResult: ...
    def choose(
        self, input: str, context: str, choices: List[str] = []
    ) -> _choose.chooseData.AnswerResult: ...
    def dialogact(self, input: str) -> _dialogact.dialogactData.DialogactResult: ...
    def paraphrase(self, input: str) -> _paraphrase.paraphraseData.ParaphraseResult: ...
    def relations(
        self, input: str, relation: Relation
    ) -> _relations.relationsData.RelationsResult: ...
    def sensibility(
        self, input: List[str] = [], history: List[Turn] = []
    ) -> _sensibility.sensibilityData.SensibilityResult: ...
    def sentiment(
        self, Client, input: str
    ) -> _sentiment.sentimentData.SentimentResult: ...
    def similarity(
        self, input: str, candidates: List[str] = []
    ) -> Optional[_similarity.similarityData.SimilarityResult]: ...
    def speak(self, Client, input: str) -> _speak.speakData.SpeakResult: ...
    def topics(
        self,
        input: Optional[str] = None,
        allow_multiple: Optional[bool] = None,
        topics: List[str] = [],
    ) -> _topics.topicsData.TopicsResult: ...
    def transcribe(self, input: str) -> _transcribe.transcribeData.TranscribeResult: ...
