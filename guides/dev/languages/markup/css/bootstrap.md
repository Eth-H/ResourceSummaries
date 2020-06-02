# grid sys
    parent
        .container
        .container-fluid //width 100%
    if no width equally spaced
    responsive to phone screens
    rm row/col inbetween spacing (margisn from .row and padding from .col)
        .no-gutters
## cols
    12 columns
    column options
        base -> specifc size (num of cols to take up) -> relative to contents
        .col .col-[1to12] .col-auto
        .col-sm .col-sm-[1to12] .col-sm-auto
        .col-md .col-md-[1to12] .col-md-auto
        .col-lg .col-lg-[1to12] .col-lg-auto
        .col-xl .col-xl-[1to12] .col-xl-auto
    wrapping
        wrapped to next line if >12 cols in the same row
    break cols to newline
        .w-100
        specifc breakpoints
            .w-100 .d-none .d-md-block
    spcific order
        .col .order-12
        .col .order-1
        .order-first (-1)
        .order-last (13)
    offset
       offset-md-6
       offset-...


## EG layout
    .container
        .row
            .col
            .col
## allignment
### vertical
    .row 
        .align-items-start
        .align-items-center
        .align-items-end
    .col
        .align-self-start
        .align-self-center
        .align-self-end
### horizontal
    .row
        .justify-content-start
        .justify-content-center
        .justify-content-end
        .justify-content-around
        .justify-content-between
# links
    https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp
    https://getbootstrap.com/docs/4.0/layout/grid/
