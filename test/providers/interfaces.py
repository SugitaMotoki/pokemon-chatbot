"""
型ヒントにTypeDictを使用
TypeDictよりもdataclassの方がいいという記事もある
"""
from typing import TypedDict, Optional, Any

import sys
from os.path import join, dirname
sys.path.append(join(dirname(__file__), "..", ".."))

from src.constants import Data


class ProviderOptions(TypedDict):
    id: Optional[str]
    config: Optional[dict[str, Any]]

class CallApiContextParams(TypedDict):
    vars: dict[str, str]

class TokenUsage(TypedDict):
    total: int
    prompt: int
    completion: int

class ProviderResponse(TypedDict):
    output: Optional[str]
    error: Optional[str]
    tokenUsage: Optional[TokenUsage]
    cost: Optional[float]
    cached: Optional[bool]
    logProbs: Optional[list[float]]

class PythonProvider:
    """
    Pythonで作成されたProviderをPromptfooで使用するためのクラス
    """


    def _call_api(self, prompt: str, options: ProviderOptions, context: CallApiContextParams):
        """
        Promptfooから呼ぶcall_apiの定義
        """

        response: ProviderResponse = {
            "output": "This is Python Provider!!!",
        }
        return response


    def get_call_api(self):
        """
        call_apiのgetter
        """
        return self._call_api


class EndToEndProvider(PythonProvider):
    """
    RAG全体の最終的な生成結果を返すProviderを使用するためのクラス
    """

    def _call_api(self, prompt: str, options: ProviderOptions, context: CallApiContextParams):
        response: ProviderResponse = {
            "output": "This is End to End Provider.",
        }
        return response


class RetrieverProvider(PythonProvider):
    """
    Retrieverによって取得されたContextを返すProviderを使用するためのクラス
    """
    def _call_api(self, prompt: str, options: ProviderOptions, context: CallApiContextParams):
        response: ProviderResponse = {
            "output": "This is Retrieval Provider.",
        }
        return response
