import os
from pathlib import Path
import numpy as np
from graphviz import Digraph

def _ensure_graphviz():
    for d in (
        r"C:\Program Files\Graphviz\bin",
        r"C:\Program Files (x86)\Graphviz\bin",
        r"C:\graphviz\bin",
    ):
        dot = Path(d) / "dot.exe"
        if dot.exists():
            os.environ["PATH"] += os.pathsep + d
            os.environ["GRAPHVIZ_DOT"] = str(dot)
            return
    raise FileNotFoundError("Graphviz 'dot.exe' not found on PATH")

_ensure_graphviz()

retrieval
d_emb = 1536
query_emb = np.random.rand(d_emb).astype(np.float32)
index_store = np.random.rand(1000, d_emb).astype(np.float32)
sims = index_store @ query_emb
top_k = 5
topk_idx = np.argsort(-sims)[:top_k]
topk_embs = index_store[topk_idx]
context_embeddings = np.vstack((query_emb, topk_embs))

attention
seq_len = context_embeddings.shape[0]
d_model = 768
num_heads = 12
d_k = d_model // num_heads
X = np.random.rand(seq_len, d_model).astype(np.float32)
W_q = np.random.rand(d_model, d_model).astype(np.float32)
W_k = np.random.rand(d_model, d_model).astype(np.float32)
W_v = np.random.rand(d_model, d_model).astype(np.float32)
W_o = np.random.rand(d_model, d_model).astype(np.float32)

def _softmax(x, axis=-1):
    e = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e / np.sum(e, axis=axis, keepdims=True)

Q = (X @ W_q).reshape(seq_len, num_heads, d_k)
K = (X @ W_k).reshape(seq_len, num_heads, d_k)
V = (X @ W_v).reshape(seq_len, num_heads, d_k)

scores = np.einsum('thd,shd->hts', Q, K) / np.sqrt(d_k)
mask = np.tril(np.ones((seq_len, seq_len), dtype=np.float32))
scores = scores * mask[None] + (-1e9) * (1 - mask)[None]
attn_weights = _softmax(scores, axis=-1)
head_out = np.einsum('hts,shd->thd', attn_weights, V)
multihead_out = head_out.reshape(seq_len, d_model)
output = multihead_out @ W_o

diagram
dot = Digraph('retrieval_attention', format='png')
dot.attr(rankdir='LR', fontsize='10')
dot.node('QE', 'query_emb\n(1536)')
dot.node('IS', 'index_store\n(1000×1536)')
dot.node('DP', 'sims\n(1000)')
dot.node('TK', 'top_k_idx')
dot.node('TKEMB', 'topk_embs')
dot.node('CTX', 'context_embeddings\n(6×1536)')
dot.node('X', 'X\n(6×768)')
dot.node('QKV', 'Q, K, V\n(6×12×64)')
dot.node('SCO', 'scores + mask')
dot.node('SM', 'attn_weights')
dot.node('HO', 'head_out')
dot.node('MHO', 'multihead_out')
dot.node('OUT', 'output')

dot.edge('QE', 'DP')
dot.edge('IS', 'DP')
dot.edge('DP', 'TK')
dot.edge('TK', 'TKEMB')
dot.edge('TKEMB', 'CTX')
dot.edge('QE', 'CTX')
dot.edge('CTX', 'X')
dot.edge('X', 'QKV')
dot.edge('QKV', 'SCO')
dot.edge('SCO', 'SM')
dot.edge('SM', 'HO')
dot.edge('HO', 'MHO')
dot.edge('MHO', 'OUT')

dot.render('retrieval_attention', view=False)

if name == "main":
    print("retrieval_attention.png generated")