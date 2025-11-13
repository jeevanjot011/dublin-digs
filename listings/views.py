from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Listing
from .forms import ListingForm
from dublindistance import calculate_distance, suggest_transport

# Browse Listings
def browse_listings(request):
    preferred_area = request.session.get('preferred_area')
    listings = Listing.objects.all().order_by('-id')

    listings_with_distance = []
    for l in listings:
        if preferred_area:
            distance_km = calculate_distance(preferred_area, l.area_code)
            transport_suggestion = suggest_transport(distance_km)
        else:
            distance_km = None
            transport_suggestion = None
        listings_with_distance.append({
            'listing': l,
            'distance': distance_km,
            'transport': transport_suggestion
        })

    return render(request, 'listings/browse.html', {
        'preferred_area': preferred_area,
        'listings_with_distance': listings_with_distance
    })


# Add Listing
def add_listing(request):
    preferred_area = request.session.get('preferred_area', 'D12')
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.save()
            # Calculate distance & suggest transport
            distance_km = calculate_distance(preferred_area, listing.area_code)
            suggestion = suggest_transport(distance_km)
            messages.success(request, f"Distance: {distance_km} km — {suggestion}")
            return redirect('browse_listings')
    else:
        form = ListingForm()
    return render(request, 'listings/add_listing.html', {'form': form})

# Edit Listing
def edit_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('browse_listings')
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/add_listing.html', {'form': form, 'edit_mode': True})

# Delete Listing
def delete_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        listing.delete()
        return redirect('browse_listings')
    return render(request, 'listings/confirm_delete.html', {'listing': listing})

# View single listing
def view_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'listings/view_listing.html', {'listing': listing})

# Set Preferred Area
def set_preferred_area(request):
    if request.method == "POST":
        area = request.POST.get("area")
        request.session["preferred_area"] = area
        messages.success(request, f"Preferred area set to {area}")
        return redirect("browse_listings")
    return render(request, "listings/set_preferred_area.html")
