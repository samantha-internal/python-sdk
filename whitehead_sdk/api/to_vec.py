#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass, field as _field
from ..schema_config.json_scalar import custom_scalars
from gql_client.runtime.variables import encode_variables
from gql import gql, Client
from gql.transport.exceptions import TransportQueryError
from functools import partial
from numbers import Number
from typing import Any, AsyncGenerator, Dict, List, Generator, Optional
from time import perf_counter
from dataclasses_json import DataClassJsonMixin, config


# fmt: off
QUERY: List[str] = ["""
query toVec($input: String!) {
  result: callNLU(input: $input) {
    has_vector
    vector
    vector_norm

    sentences {
      has_vector
      vector
      vector_norm

      entities {
        has_vector
        vector
        vector_norm

        entities {
          has_vector
          vector
          vector_norm

          entities {
            has_vector
            vector
            vector_norm

            entities {
              has_vector
              vector
              vector_norm
            }
          }
        }
      }
    }

    noun_chunks {
      has_vector
      vector
      vector_norm

      entities {
        has_vector
        vector
        vector_norm

        entities {
          has_vector
          vector
          vector_norm

          entities {
            has_vector
            vector
            vector_norm

            entities {
              has_vector
              vector
              vector_norm
            }
          }
        }
      }
    }

    entities {
      has_vector
      vector
      vector_norm

      entities {
        has_vector
        vector
        vector_norm

        entities {
          has_vector
          vector
          vector_norm

          entities {
            has_vector
            vector
            vector_norm

            entities {
              has_vector
              vector
              vector_norm
            }
          }
        }
      }
    }
  }
}

# FIXME: Unfortunately, fragments are not supported by either codegen framework

# fragment EntityResultFields on NLUResult {
#   has_vector
#   vector
#   vector_norm
# }
#
# fragment EntityFields on NLUSpan {
#   has_vector
#   vector
#   vector_norm
# }
#
# fragment EntitySubtree on NLUSpan {
#   ...EntityFields
#   entities {
#     ...EntityFields
#     entities {
#       ...EntityFields
#       entities {
#         ...EntityFields
#         entities {
#           ...EntityFields
#         }
#       }
#     }
#   }
# }

"""
]


class toVec:
    @dataclass(frozen=True)
    class toVecData(DataClassJsonMixin):
        @dataclass(frozen=True)
        class NLUResult(DataClassJsonMixin):
            @dataclass(frozen=True)
            class NLUSpan(DataClassJsonMixin):
                @dataclass(frozen=True)
                class NLUSpan(DataClassJsonMixin):
                    @dataclass(frozen=True)
                    class NLUSpan(DataClassJsonMixin):
                        @dataclass(frozen=True)
                        class NLUSpan(DataClassJsonMixin):
                            @dataclass(frozen=True)
                            class NLUSpan(DataClassJsonMixin):
                                has_vector: Optional[bool]
                                vector: Optional[List[Number]]
                                vector_norm: Optional[Number]

                            has_vector: Optional[bool]
                            vector: Optional[List[Number]]
                            vector_norm: Optional[Number]
                            entities: Optional[List[NLUSpan]]

                        has_vector: Optional[bool]
                        vector: Optional[List[Number]]
                        vector_norm: Optional[Number]
                        entities: Optional[List[NLUSpan]]

                    has_vector: Optional[bool]
                    vector: Optional[List[Number]]
                    vector_norm: Optional[Number]
                    entities: Optional[List[NLUSpan]]

                has_vector: Optional[bool]
                vector: Optional[List[Number]]
                vector_norm: Optional[Number]
                entities: Optional[List[NLUSpan]]

            has_vector: Optional[bool]
            vector: Optional[List[Number]]
            vector_norm: Optional[Number]
            sentences: Optional[List[NLUSpan]]
            noun_chunks: Optional[List[NLUSpan]]
            entities: Optional[List[NLUSpan]]

        result: Optional[NLUResult]

    # fmt: off
    @classmethod
    def execute(cls, client: Client, input: str) -> Optional[toVecData.NLUResult]:
        variables: Dict[str, Any] = {"input": input}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = client.execute(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.toVecData.from_dict(response_text)
        return res.result

    # fmt: off
    @classmethod
    async def execute_async(cls, client: Client, input: str) -> Optional[toVecData.NLUResult]:
        variables: Dict[str, Any] = {"input": input}
        new_variables = encode_variables(variables, custom_scalars)
        response_text = await client.execute_async(
            gql("".join(set(QUERY))), variable_values=new_variables
        )
        res = cls.toVecData.from_dict(response_text)
        return res.result