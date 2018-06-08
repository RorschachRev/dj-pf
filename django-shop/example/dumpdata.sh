#!/bin/sh
[ -z "$DJANGO_SHOP_TUTORIAL" ] && echo "Environment variable DJANGO_SHOP_TUTORIAL is not set" && exit 1
mkdir -p ../workdir/$DJANGO_SHOP_TUTORIAL/fixtures
./manage.py dumpdata --indent=2 --natural-foreign email_auth cms cmsplugin_cascade djangocms_text_ckeditor filer post_office shop myshop --exclude cmsplugin_cascade.segmentation --exclude filer.clipboard --exclude filer.clipboarditem --exclude myshop.order --exclude myshop.orderpayment --exclude myshop.orderitem --exclude myshop.cart --exclude myshop.cartitem > ../workdir/$DJANGO_SHOP_TUTORIAL/fixtures/myshop.json
