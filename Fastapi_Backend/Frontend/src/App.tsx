import { useState, useEffect } from 'react'

interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  quantity: number;
}

function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({ name: '', price: '', description: '', quantity: '' });

  const fetchProducts = async () => {
    try {
      const res = await fetch('http://localhost:8000/products');
      const data = await res.json();
      setProducts(data);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const addProduct = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:8000/products', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: formData.name,
          price: parseFloat(formData.price),
          description: formData.description,
          quantity: parseInt(formData.quantity)
        }),
      });
      if (res.ok) {
        setFormData({ name: '', price: '', description: '', quantity: '' });
        fetchProducts();
      }
    } catch (e) {
      console.error(e);
    }
  };

  const deleteProduct = async (id: number) => {
    try {
      const res = await fetch(`http://localhost:8000/products/${id}`, { method: 'DELETE' });
      if (res.ok) {
        fetchProducts();
      }
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div className="min-h-screen bg-[#0f172a] text-slate-200 p-8 font-sans pb-24">
      <div className="max-w-4xl mx-auto space-y-12">
        <header className="text-center space-y-4">
          <h1 className="text-5xl font-extrabold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-indigo-500 pb-2">
            Inventory Dashboard
          </h1>
          <p className="text-slate-400 text-lg">Manage your products with a beautiful API-driven interface.</p>
        </header>

        <main className="grid md:grid-cols-12 gap-8">
          {/* Add Product Form */}
          <div className="md:col-span-5 bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 shadow-[0_8px_30px_rgb(0,0,0,0.12)]">
            <h2 className="text-xl font-bold mb-6 text-white tracking-wide">Add New Product</h2>
            <form onSubmit={addProduct} className="space-y-5">
              <div>
                <label className="block text-sm font-medium text-slate-400 mb-1">Name</label>
                <input
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  required
                  className="w-full bg-slate-900/50 border border-slate-700/50 rounded-xl px-4 py-2.5 outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all text-sm placeholder-slate-500"
                  placeholder="e.g. Wireless Mouse"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-400 mb-1">Description</label>
                <textarea
                  name="description"
                  value={formData.description}
                  onChange={handleChange}
                  required
                  rows={2}
                  className="w-full bg-slate-900/50 border border-slate-700/50 rounded-xl px-4 py-2.5 outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all text-sm placeholder-slate-500 resize-none"
                  placeholder="A short description..."
                />
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-slate-400 mb-1">Price ($)</label>
                  <input
                    name="price"
                    type="number"
                    step="0.01"
                    min="0"
                    value={formData.price}
                    onChange={handleChange}
                    required
                    className="w-full bg-slate-900/50 border border-slate-700/50 rounded-xl px-4 py-2.5 outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all text-sm placeholder-slate-500"
                    placeholder="0.00"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-400 mb-1">Quantity</label>
                  <input
                    name="quantity"
                    type="number"
                    min="0"
                    value={formData.quantity}
                    onChange={handleChange}
                    required
                    className="w-full bg-slate-900/50 border border-slate-700/50 rounded-xl px-4 py-2.5 outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all text-sm placeholder-slate-500"
                    placeholder="0"
                  />
                </div>
              </div>
              <button
                type="submit"
                className="w-full mt-4 bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-400 hover:to-purple-500 text-white font-medium py-3 rounded-xl shadow-lg hover:shadow-indigo-500/25 transition-all outline-none"
              >
                Create Product
              </button>
            </form>
          </div>

          {/* Product List */}
          <div className="md:col-span-7 space-y-4">
            <h2 className="text-xl font-bold mb-6 text-white tracking-wide">Current Inventory</h2>
            {loading ? (
              <div className="animate-pulse space-y-4">
                {[...Array(3)].map((_, i) => (
                  <div key={i} className="h-28 bg-white/5 rounded-2xl border border-white/5 rounded"></div>
                ))}
              </div>
            ) : products.length === 0 ? (
              <div className="text-center bg-white/5 border border-white/5 rounded-2xl p-10 flex flex-col items-center">
                <span className="text-4xl mb-4">📦</span>
                <h3 className="text-lg font-medium text-slate-300">No products found</h3>
                <p className="text-slate-500 mt-2">Add a product to get started.</p>
              </div>
            ) : (
              <div className="grid gap-4">
                {products.map((p) => (
                  <div key={p.id} className="group relative bg-white/5 hover:bg-white/10 border border-white/5 hover:border-white/10 rounded-2xl p-5 flex flex-col justify-between transition-all">
                    <div className="flex justify-between items-start gap-4">
                      <div>
                        <h3 className="text-lg font-semibold text-white group-hover:text-indigo-300 transition-colors">{p.name}</h3>
                        <p className="text-sm text-slate-400 mt-1 mb-3 line-clamp-2">{p.description}</p>
                      </div>
                      <div className="text-right flex-shrink-0">
                        <span className="text-xl font-bold text-emerald-400">${p.price.toFixed(2)}</span>
                        <div className="text-xs text-slate-500 mt-1 uppercase font-semibold">Qty: {p.quantity}</div>
                      </div>
                    </div>
                    
                    <div className="absolute opacity-0 group-hover:opacity-100 transition-opacity top-4 right-4">
                      
                    </div>
                    <div className="mt-2 pt-4 border-t border-white/5 flex justify-end">
                       <button
                          onClick={() => deleteProduct(p.id)}
                          className="text-xs font-semibold uppercase tracking-wider text-rose-400/80 hover:text-rose-400 hover:bg-rose-400/10 px-3 py-1.5 rounded-lg transition-colors"
                        >
                          Remove
                        </button>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </main>
      </div>
    </div>
  )
}

export default App
