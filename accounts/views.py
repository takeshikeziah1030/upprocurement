import csv, io
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .models import Procurement
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, ProcurementForm, NewRequestForm
from django.http import HttpResponse
from django.views.generic.edit import UpdateView 
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from .filters import ProcurementFilter
from django.db.models import Count, Avg

# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user  )
            return redirect('accounts:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:intro')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logoutUSer(request):
    logout(request)
    return redirect('accounts:login')

@permission_required('admin.can_add_log_entry')
def upload(request):
    template = 'upload.html'

    prompt = {
        'order': 'Upload, Procurement Dataset:'
    }
    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload only csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, quotechar='|'):
        _, created = Procurement.objects.update_or_create(
            Equipment= column[0],
            PONo= column[1],
            Delivery_Terms = column[2],
            Budget = column[3],
            PPMP_Date = column[4],
            PPMP_Signatures = column[5],
            PPMP_Pages = column[6],
            PPMP_Days = column[7],
            PR_Date = column[8],
            PR_Signatures = column[9],
            PR_Pages = column[10],
            PR_Days = column[11],
            Pre_Bid_Date = column[12],
            Pre_Bid_Signatures = column[13],
            Pre_Bid_Pages = column[14],
            Pre_Bid_Days =column[15],
            Opening_Bid_Date = column[16],
            Opening_Bid_Signatures = column[17],
            Opening_Bid_Pages = column[18],
            Opening_Bid_Days = column[19],
            Post_Qual_Date = column[20],
            Post_Qual_Signatures = column[21],
            Post_Qual_Pages = column[22],
            Post_Qual_Days = column[23],
            NOA_Date = column[24],
            NOA_Signatures = column[25],
            NOA_Pages = column[26],
            NOA_Days = column[27],
            PO_Date = column[28],
            PO_Signatures = column[29],
            PO_Pages = column[30],
            PO_Days = column[31],
            PO_Approval_Date = column[32],
            PO_Approval_Signatures = column[33],
            PO_Approval_Pages = column[34],
            PO_Approval_Days = column[35],
            PO_Supplier_Date = column[36],
            PO_Supplier_Signatures = column[37],
            PO_Supplier_Pages = column[38],
            PO_Supplier_Days = column[39],
            Delivery_Date = column[40],
            Delivery_Signatures = column[41],
            Delivery_Pages = column[42],
            Delivery_Days = column[43],
            DV_Processing_Date = column[44],
            DV_Signatures = column[45],
            DV_Pages = column[46],
            DV_Days = column[47],
            DV_Approval_Date = column[48],
            DV_Approval_Signatures = column[49],
            DV_Approval_Pages = column[50],
            DV_Approval_Days = column[51],
            OR_CR_Request_Date = column[52],
            OR_CR_Signatures = column[53],
            OR_CR_Pages = column[54],
            OR_CR_Days = column[55],
            Check_Releasing_Date = column[56],
            Check_Signatures = column[57],
            Check_Pages = column[58],
            Check_Days = column[59],
            Total_LeadTime = column[60],
            Total_Signatures = column[61],
        )
    context = {}
    return redirect('accounts:list')

class ProcurementList(ListView):
    template_name = 'list.html'
    model = Procurement

class CompleteList(ListView):
    template_name = 'complete.html'
    model = Procurement
    procurement = Procurement.objects.all()
    pending = Procurement.objects.filter(Status='Pending').count()
    ongoing = Procurement.objects.filter(Status='Approved').count()
    complete = Procurement.objects.filter(Status='Completed').count()
    #total_days = Procurement.objects.all().aggregate(Avg('Total_LeadTime'))
    #myFilter = ProcurementFilter(request.GET, queryset=procurement)
    #procurement= myFilter.qs
    #success_url = reverse_lazy('accounts:reports', context)
    #context = {'procurement':procurement, 'pending':pending, 'ongoing':ongoing, 'complete':complete}
    #return render(request, 'reports.html', context)

class ProcurementDetail(DetailView):
    context_object_name = 'obj'
    template_name = 'details.html'
    model = Procurement

class ProcurementCreateView(CreateView):
    form_class = NewRequestForm
    template_name = 'new.html'
    queryset = NewRequestForm
    success_url = reverse_lazy('accounts:')

class ProcurementUpdateView(UpdateView):  
    form_class = ProcurementForm
    template_name = 'update.html'
    queryset = ProcurementForm
    success_url = reverse_lazy('accounts:list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Procurement, pk=pk)

class ProcurementDeleteView(DeleteView):
    template_name = "delete.html"
    success_url = reverse_lazy('accounts:list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Procurement, pk=pk)

class introView(TemplateView):
    template_name = "intro.html"
    success_url = reverse_lazy('accounts:intro')

class PendingList(ListView):
    template_name = 'request.html'
    model = Procurement

class PendingUpdateView(UpdateView):  
    form_class = NewRequestForm
    template_name = 'update.html'
    queryset = NewRequestForm
    success_url = reverse_lazy('accounts:list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Procurement, pk=pk)


def reports(request):
    procurement = Procurement.objects.all()
    pending = Procurement.objects.filter(Status='Pending').count()
    ongoing = Procurement.objects.filter(Status='On-Going').count()
    complete = Procurement.objects.filter(Status='Completed').count()
    Purchase_Order = Procurement.objects.filter(Types_of_Procurement='Purchase-Order').count()
    Special_Procurement = Procurement.objects.filter(Types_of_Procurement='Repeat-Order').count()
    Above1M = Procurement.objects.filter(Types_of_Procurement='Bidding-1M-and-Above').count()
    Less1M = Procurement.objects.filter(Types_of_Procurement='Bidding-Less-Than-1M').count()
    Direct = Procurement.objects.filter(Types_of_Procurement='Direct-Contracting').count()
    context = {'procurement':procurement, 'pending':pending, 'ongoing':ongoing, 'complete':complete,
    'Direct':Direct, 'Purchase_Order':Purchase_Order, 'Special_Procurement':Special_Procurement, 
    'Above1M':Above1M, 'Less1M':Less1M}
    return render(request, 'reports.html', context)

def charts(request):
    context= {}
    return render(request, 'chart.html', context)

   

