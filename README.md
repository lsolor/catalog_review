
**Services (default ports)**
- API: http://localhost:8000
- Postgres: localhost:5432
- Redis: localhost:6379
- Redpanda (Kafka): localhost:9092 — Console: http://localhost:8081
- OpenSearch: http://localhost:9200 — Dashboards: http://localhost:5601
- Jaeger: http://localhost:16686
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

---

## Prereqs

- Docker Desktop (or Docker Engine) and Docker Compose
- Python 3.12+ (`uv` or `poetry` recommended)
- Make (optional)
- cURL or HTTP client (e.g., HTTPie, Postman)

---

## Quick Start

1. **Configure environment**
   - Copy `.env.example` → `.env.local` and set values (DB URL, Redis URL, Kafka bootstrap server).
2. **Start infra**
   - `docker compose up -d` (brings up Postgres, Redis, Redpanda, OpenSearch, Jaeger, Prometheus, Grafana).
3. **Run API & workers**
   - Start the API container (FastAPI) and two worker containers (Indexer, Trending).
4. **Seed data (optional)**
   - Run the seed script to create users/products/reviews.
5. **Open UIs**
   - API docs: `http://localhost:8000/docs`
   - Redpanda Console: `http://localhost:8081`
   - OpenSearch Dashboards: `http://localhost:5601`
   - Jaeger: `http://localhost:16686`
   - Grafana: `http://localhost:3000` (import dashboards from `docs/grafana/`)

## Development

1. **UV Local**
   - uv run fastapi dev main.py --host 0.0.0.0 --port 8000
2. **Start infra**
   - `docker compose up -d` (brings up Postgres, Redis, Redpanda, OpenSearch, Jaeger, Prometheus, Grafana).
3. **Run API & workers**
   - Start the API container (FastAPI) and two worker containers (Indexer, Trending).
4. **Seed data (optional)**
   - Run the seed script to create users/products/reviews.
5. **Open UIs**
   - API docs: `http://localhost:8000/docs`
   - Redpanda Console: `http://localhost:8081`
   - OpenSearch Dashboards: `http://localhost:5601`
   - Jaeger: `http://localhost:16686`
   - Grafana: `http://localhost:3000` (import dashboards from `docs/grafana/`)

---

## Domain & API (v1)

**Entities**
- **Product**: `id`, `name`, `description`, `category`, `price`, timestamps
- **Review**: `id`, `product_id`, `user_id`, `rating`, `text`, timestamp
- **User**: `id`, `email`

**Core endpoints**
- `POST /v1/products` – create
- `GET /v1/products?category=&q=&page=&page_size=` – list & filter
- `GET /v1/products/{id}` – detail (cached)
- `PATCH /v1/products/{id}` – update (invalidates cache, emits event)
- `POST /v1/reviews` – create review (rate limited, emits event)
- `GET /v1/products/{id}/reviews` – list reviews
- `GET /v1/search?q=&category=&sort=` – OpenSearch‑backed search
- `GET /v1/products/trending?window=24h|7d&limit=10` – Redis ZSET‑backed

**Auth**
- Simple JWT bearer (`Authorization: Bearer <token>`). Dev secret only.

---

## Events & Topics

**Topics**
- `product-updated` (key = `product_id`)
- `review-created` (key = `product_id`)
- `dlq.product-updated`, `dlq.review-created`

**Event envelope (JSON)**
```json
{
  "version": 1,
  "event_type": "product-updated",
  "product_id": "uuid",
  "payload": { "name": "Widget A", "category": "gadgets", "price": 19.99 },
  "ts": "2025-08-23T21:00:00Z",
  "request_id": "req-123"
}
