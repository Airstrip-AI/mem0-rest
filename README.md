# Dockerized Mem0 REST APIs

This is an **unofficial** dockerized api server that wraps around Mem0's [open-source python project](https://github.com/mem0ai/mem0).

## Getting started

This project requires an OpenAI API key to work. Support for other providers is not implemented yet.

First,

```
cp sample.env .env
```

Edit `.env` and replace the dummy value for `OPENAI_API_KEY` with an actual value. Then,

```
docker compose up
# The server is now running at http://localhost:4321
```

## Motivation

We are using Mem0 for our project at https://github.com/Airstrip-AI/airstrip (Typescript). In order to provide a fully open-source project, we need an API server i.e. "an open-source version of Mem0 cloud". We searched and did not find one, hence we built this.

If you are not building on Python, but want to try out Mem0 locally, hope this helps!

## API (dis)parity

We tried to keep it as close to [Mem0's cloud APIs](https://docs.mem0.ai/api-reference/overview) as possible, but there are still some differences between the API spec and the Python function calls. This shouldn't be treated as a 1:1 mapping of the cloud APIs, instead it is simply a wrapper over [the function calls](https://github.com/mem0ai/mem0/blob/main/mem0/memory/main.py#L27).

### Graph DB

Not supported yet. This project spins up a Mem0 server and Qdrant for the vector database only.

### Usage

#### Add a memory

```
curl --request POST \
  --url http://localhost:4321/v1/memories \
  --header 'Content-Type: application/json' \
  --data '{
    "messages": [
      {
        "role": "user",
        "content": "I am working on improving my tennis skills. Suggest some online courses."
      }
    ],
    "user_id": "user1",
    "agent_id": "app1",
    "metadata": {"category": "hobbies"}
  }'
```

#### Update a memory

```
curl --request PUT \
  --url http://localhost:4321/v1/memories/<memory_id> \
  --header 'Content-Type: application/json' \
  --data '{"data": "Likes to play tennis on weekends"}'
```

#### Search for memories

```
curl --request POST \
 --url http://localhost:4321/v1/memories/search \
 --header 'Content-Type: application/json' \
 --data '{"query": "What are Alice'\''s hobbies?", "user_id": "user1"}'
```

#### Get all memories

```
curl http://localhost:4321/v1/memories
```

#### Get a memory's history

```
curl http://localhost:4321/v1/memories/<memory_id>/history
```
