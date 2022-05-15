# from multiprocessing import context
# from django.shortcuts import render
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView,DeleteView
# from django.urls import reverse_lazy
# from watchlists_api.models import UserWatchlist, WatchlistStocks

# from django.contrib.auth.mixins import LoginRequiredMixin

# # Create your views here.


# class WatchList(LoginRequiredMixin, ListView):
#     model = UserWatchlist
#     context_object_name ='watchlists'
#     template_name = 'watchlist/watchlists.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs) 
#         context ['watchlists'] = context ['watchlists'].filter(user = self.request.user)
        
#         search_input = self.request.GET.get('search-area') or ''
#         if search_input:
#             context['watchlists'] = context['watchlists'].filter(name__startswith=search_input)
        
#         context['search_input'] = search_input
        
#         return context
    

# class WatchlistDetail(LoginRequiredMixin, DetailView):
#     model = UserWatchlist
#     template_name = 'watchlist/watchlist_stocks.html'
#     context_object_name = 'details'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['stocks'] = WatchlistStocks.objects.filter(watchlistid_id = context['details'].id)
#         return context
    
    
# class WatchlistCreate(LoginRequiredMixin, CreateView):
#     model = UserWatchlist
#     fields = ['name', 'Description']
#     success_url = reverse_lazy('watchlists') #to be edited later
#     def form_valid(self,form):
#         form.instance.user = self.request.user
#         return super(WatchlistCreate, self).form_valid(form)
    
    
# class WatchliststocksCreate(CreateView):
#     model = WatchlistStocks
#     fields = '__all__'
#     success_url = reverse_lazy('watchlists')
    


    
# class WatchlistUpdate(LoginRequiredMixin, UpdateView):
#     model = UserWatchlist
#     fields = ['name', 'Description']
#     success_url = reverse_lazy('watchlists') #to be edited later
    
# class WatchliststockUpdate(LoginRequiredMixin, UpdateView):
#     model = WatchlistStocks
#     fields = '__all__'
#     success_url = reverse_lazy('watchlists')
    
# class WatchlistDelete(LoginRequiredMixin, DeleteView):
#     model = UserWatchlist
#     context_object_name = 'watchlist'
#     success_url = reverse_lazy('watchlists') #to be edited later