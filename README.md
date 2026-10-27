# 120 Days: From Scripts to Shipped AI SaaS

> A daily execution plan to go from "I know variables, functions and loops" to building and deploying a full-stack, AI-powered product.

**Time:** 2-3 hours/day | **Timeline:** 120 Days | **Outcome:** 1 Deployed SaaS + RAG Chatbot + 7 Portfolio Projects
**Dashboard:** [Live Daily Roadmap - Hosted on GitHub Pages]

---

## 📚 Source Books

This roadmap distills 5 books (~2,800 pages) into 120 actionable days:

1. **Python Crash Course (3rd Ed)** - Eric Matthes - *Foundation & Projects*
2. **Learn Python Programming (3rd Ed)** - Fabrizio Romano - *Deep Python*
3. **Python Object-Oriented Programming (4th Ed)** - Lott & Phillips - *Architecture*
4. **FastAPI, React, MongoDB** - Marko et al. - *Full-Stack Product*
5. **LLM Engineer's Handbook** - Paul Iusztin & Maxime Labonne - *AI Engineering*

> **Starting Point:** You already know variables, functions, loops. We skip the absolute basics.

---

## 🗺️ Roadmap Overview

| Phase | Days | Book | Goal | Main Project |
| :--- | :--- | :--- | :--- | :--- |
| **1. Foundation Sprint** | 1-21 | Crash Course | Classes, Files, Testing, APIs | CLI File Analyzer + Weather Viz |
| **2. Deep Python** | 22-42 | Learn Python Programming | Decorators, Generators, Async | Async Web Scraper |
| **3. Architecture** | 43-63 | OOP 4th Edition | SOLID, Patterns, Typing | Refactored Clean Package |
| **4. Full-Stack Product** | 64-98 | FastAPI React MongoDB | APIs, Auth, React, Docker | **TaskFlow SaaS (Deployed)** |
| **5. LLM Engineer** | 99-120 | LLM Handbook | RAG, Vector DBs, Eval | RAG Chatbot for TaskFlow |

**Daily Rhythm:** 60m Read + 90m Build + 15m Recap. Code > Notes.

---

## ✅ 120-Day Daily Checklist

Copy this into your issues or use as commit checklist.

### Phase 1: Foundation Sprint (Days 1-21) - Python Crash Course

#### Skips Ch 1-8, Skips Pygame Ch 12-14

- [ ] **Day 1:** Ch 9 - Classes basics. Build: `Restaurant` class
- [ ] **Day 2:** Ch 9 - Inheritance & Composition. Build: `Admin` inherits from `User`
- [ ] **Day 3:** Ch 9 - Importing Classes. Mini-Project: Modular class library
- [ ] **Day 4:** Ch 10 - Files: Reading files, handling large files
- [ ] **Day 5:** Ch 10 - Writing, JSON, storing user data
- [ ] **Day 6:** Ch 10 - Exceptions, fail silently, refactoring
- [ ] **Day 7:** **Project:** CLI File Analyzer - counts words, handles errors, saves JSON report
- [ ] **Day 8:** Ch 11 - Testing: unittest, passing/failing tests
- [ ] **Day 9:** Ch 11 - Testing Classes, fixtures
- [ ] **Day 10:** **Project:** Write full tests for Day 7 CLI
- [ ] **Day 11:** Ch 15 - Matplotlib, scatter, random walks
- [ ] **Day 12:** Ch 15 - Rolling dice, styling plots
- [ ] **Day 13:** Ch 16 - CSV: Reading Lagos/Nigeria weather data
- [ ] **Day 14:** Ch 16 - JSON: Earthquake mapping
- [ ] **Day 15:** **Project:** Weather Dashboard with Matplotlib + CSV
- [ ] **Day 16:** Ch 17 - APIs: `requests`, status codes
- [ ] **Day 17:** Ch 17 - GitHub API, HackerNews API - Build API client
- [ ] **Day 18:** Ch 18 - Django Intro: Setup, project vs app
- [ ] **Day 19:** Ch 18-19 - Models, Admin, Django Shell
- [ ] **Day 20:** Ch 19 - Views, Templates, Forms
- [ ] **Day 21:** **Phase Review:** Deploy mini blog to PythonAnywhere + retrospective

### Phase 2: Deep Python (Days 22-42) - Learn Python Programming

- [ ] **Day 22:** Iterators & Iterables: `__iter__`, `__next__`
- [ ] **Day 23:** Generators: `yield`, generator expressions, performance
- [ ] **Day 24:** **Build:** Generator-based log parser for large files
- [ ] **Day 25:** Decorators 101: Functions as objects, wrapper pattern
- [ ] **Day 26:** Decorators with arguments, stacking, `functools.wraps`
- [ ] **Day 27:** **Build:** `@timer`, `@retry`, `@cache` decorator library
- [ ] **Day 28:** Context Managers: `with`, `__enter__/__exit__`, `contextlib`
- [ ] **Day 29:** Functions Deep Dive: closures, scoping, `*args/**kwargs`
- [ ] **Day 30:** **Build:** Config manager using context managers
- [ ] **Day 31:** Modules & Packages: `__init__.py`, relative imports, `venv`
- [ ] **Day 32:** OOP Recap: `__dunder__` methods, magic methods
- [ ] **Day 33:** Functional: `map`, `filter`, `lambda`, `itertools`
- [ ] **Day 34:** Collections: `namedtuple`, `Counter`, `defaultdict`
- [ ] **Day 35:** Concurrency 1: Threading vs Multiprocessing
- [ ] **Day 36:** Concurrency 2: `asyncio`, `async/await`, `aiohttp`
- [ ] **Day 37:** Testing Deep Dive: `pytest`, fixtures, mocking
- [ ] **Day 38:** Typing: `typing`, `mypy`, type hints
- [ ] **Day 39:** Project Setup: Structure a real Python package
- [ ] **Day 40:** **Project Start:** Async Web Scraper with rate limiting
- [ ] **Day 41:** Scraper: Add decorators for caching, retries, async gathering
- [ ] **Day 42:** **Project Finish:** Tests + README + publish to GitHub

### Phase 3: Architecture (Days 43-63) - Python OOP 4th Edition

- [ ] **Day 43:** SOLID - Single Responsibility & Open/Closed
- [ ] **Day 44:** SOLID - Liskov, Interface Segregation, Dependency Inversion
- [ ] **Day 45:** Class Design: When to use composition over inheritance
- [ ] **Day 46:** **Build:** Refactor Phase 2 scraper using SOLID
- [ ] **Day 47:** Dataclasses, `attrs`, properties, descriptors
- [ ] **Day 48:** Typing Advanced: Protocols, Generics
- [ ] **Day 49:** Creational Patterns: Factory, Builder, Singleton (and why to avoid)
- [ ] **Day 50:** Structural Patterns: Adapter, Decorator (pattern), Facade
- [ ] **Day 51:** Behavioral Patterns: Observer, Strategy, State
- [ ] **Day 52:** **Build:** Implement 3 patterns in a payment processor example
- [ ] **Day 53:** Inheritance vs Mixins vs ABCs
- [ ] **Day 54:** Error Handling Architecture: Custom exceptions
- [ ] **Day 55:** Persistence: ORM concepts, serialization
- [ ] **Day 56:** Testing OOP: Mocking, dependency injection for tests
- [ ] **Day 57:** Documentation: Docstrings, Sphinx
- [ ] **Day 58:** Performance: Slots, profiling, optimization
- [ ] **Day 59:** **Project Start:** Plugin System - define interface
- [ ] **Day 60:** Plugin System: Implement 3 plugins using patterns
- [ ] **Day 61:** Plugin System: Add config, dynamic loading
- [ ] **Day 62:** Refactor ALL previous projects with new architecture
- [ ] **Day 63:** **Phase Review:** Write ARCHITECTURE.md doc

### Phase 4: Full-Stack Product (Days 64-98) - FastAPI, React, MongoDB

#### This is the main portfolio piece

- [ ] **Day 64:** FastAPI Intro: `uvicorn`, path ops, Pydantic models
- [ ] **Day 65:** Routing, dependency injection, project structure
- [ ] **Day 66:** MongoDB & Beanie ODM: Models, connection
- [ ] **Day 67:** CRUD: Create & Read endpoints for Tasks
- [ ] **Day 68:** CRUD: Update & Delete, validation, error handling
- [ ] **Day 69:** **Build:** Task API v1 - test with Swagger UI
- [ ] **Day 70:** Auth Concepts: Hashing with `passlib`, JWT structure
- [ ] **Day 71:** Auth: Register endpoint, login, access token
- [ ] **Day 72:** Auth: Protected routes, `get_current_user` dependency
- [ ] **Day 73:** Auth: Refresh tokens, user model in MongoDB
- [ ] **Day 74:** **Build:** Full Auth flow - Postman collection
- [ ] **Day 75:** React Intro: Vite, components, props, state
- [ ] **Day 76:** React Hooks: `useState`, `useEffect`, `useContext`
- [ ] **Day 77:** React Router, protected routes, login page
- [ ] **Day 78:** API Integration: `axios`, calling FastAPI from React
- [ ] **Day 79:** **Build:** Frontend Auth - login/register UI working
- [ ] **Day 80:** Task UI: List, Create, Edit, Delete components
- [ ] **Day 81:** State Management: Context or Zustand for tasks
- [ ] **Day 82:** Forms: `react-hook-form`, validation, error display
- [ ] **Day 83:** Styling: Tailwind CSS, responsive layout
- [ ] **Day 84:** **Build:** Full CRUD UI connected to API
- [ ] **Day 85:** Advanced API: Pagination, filtering, sorting
- [ ] **Day 86:** File Uploads, background tasks
- [ ] **Day 87:** Testing: Pytest for API, Vitest for React
- [ ] **Day 88:** **Build:** Add search & filters to TaskFlow
- [ ] **Day 89:** Docker: Dockerfile for FastAPI, Dockerfile for React
- [ ] **Day 90:** Docker Compose: Full stack locally
- [ ] **Day 91:** Deploy Backend: Fly.io / Render setup
- [ ] **Day 92:** Deploy Frontend: Vercel, env vars
- [ ] **Day 93:** Deploy DB: MongoDB Atlas, connection strings
- [ ] **Day 94:** CI/CD: GitHub Actions for lint/test
- [ ] **Day 95:** Polish: Loading states, empty states, toasts
- [ ] **Day 96:** README: Demo GIF, architecture diagram, API docs
- [ ] **Day 97:** **Project Finish:** TaskFlow SaaS v1 Live
- [ ] **Day 98:** Phase Review: Record 2-min demo video for portfolio

### Phase 5: LLM Engineer (Days 99-120) - LLM Engineer's Handbook

#### Adds AI to your SaaS

- [ ] **Day 99:** LLM Fundamentals: Tokens, embeddings, prompt engineering
- [ ] **Day 100:** OpenAI API: Completion vs Chat, streaming, function calling
- [ ] **Day 101:** Vector DBs: Chroma vs Qdrant, cosine similarity, indexing
- [ ] **Day 102:** RAG Concept: Ingestion, chunking strategies
- [ ] **Day 103:** **Build:** Setup Qdrant locally, embed sample docs
- [ ] **Day 104:** Chunking: `langchain` text splitters, overlap, metadata
- [ ] **Day 105:** Embeddings: OpenAI vs open-source (Sentence-Transformers)
- [ ] **Day 106:** Retrieval: Similarity search, top-k, reranking
- [ ] **Day 107:** **Build:** RAG pipeline script - PDF -> chunks -> Qdrant -> query
- [ ] **Day 108:** RAG Integration: Create `/chat` endpoint in FastAPI
- [ ] **Day 109:** Prompt Templates: System prompts, context injection
- [ ] **Day 110:** Frontend Chat UI: Chat component, streaming responses
- [ ] **Day 111:** **Build:** Chat with your tasks/docs - working in TaskFlow
- [ ] **Day 112:** Evaluation: RAGAS, checking hallucinations, grounding
- [ ] **Day 113:** Guardrails: Input validation, output filtering, rate limiting
- [ ] **Day 114:** Optimization: Caching embeddings, latency, cost
- [ ] **Day 115:** Alternative LLMs: Ollama, local models
- [ ] **Day 116:** Monitoring: Logging LLM calls, tracing
- [ ] **Day 117:** **Build:** Final AI feature - "Summarize my tasks" button
- [ ] **Day 118:** Docs & Polish: Update README with RAG architecture diagram
- [ ] **Day 119:** Portfolio: LinkedIn post, demo video v2, blog post
- [ ] **Day 120:** **GRADUATION:** Final retrospective, plan next 60 days, deploy v2

---

## 📂 Suggested Repo Structure

``` python
/120-days-from-scripts-to-shipped-ai-saas
├── README.md (this file)
├── docs/
│   └── roadmap.html (daily dashboard)
├── phase-1-foundation/
│   ├── cli-file-analyzer/
│   └── weather-dashboard/
├── phase-2-deep-python/
│   ├── decorator-library/
│   └── async-scraper/
├── phase-3-architecture/
│   └── plugin-system/
├── phase-4-fullstack/
│   └── taskflow-saas/
│       ├── backend/ (FastAPI)
│       ├── frontend/ (React)
│       └── docker-compose.yml
└── phase-5-llm/
    └── taskflow-rag/
        ├── ingestion/
        └── qdrant/
```

## 🚀 How to Use This Repo

1. Clone and check off tasks daily in this README
2. Each day: `git commit -m "Day X: <what you built>"`
3. Push daily - learning in public builds accountability
4. Host your daily dashboard on GitHub Pages

## 🎯 Definition of Done (Day 120)

- [ ] TaskFlow SaaS deployed and live (Frontend + Backend + DB)
- [ ] Auth working (Register/Login/JWT)
- [ ] RAG Chatbot integrated that answers over your tasks/docs
- [ ] Demo video (2 min) + Architecture diagram
- [ ] README with live links

---

**Built by Udoh Lawrence** | Started: Oct 2026 | Goal: Ship one real AI product in 120 days.

> If you're following along, star this repo and open an issue with your Day 1 commit!
