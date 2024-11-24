import streamlit as st

st.title('Sourdough Calculator')

st.markdown("Specify the amount of flour (gr), yeast (gr), the corresponding yeast hydration (%), and the amount of salt (%) (relative to the amount of flour) in the fields below:")

# Input fields
flour = st.number_input(r'FLOUR (gr)', value=500, step=10)
yeast = st.number_input(r'YEAST (gr)', value=100, step=1)
yeast_hydration = st.number_input(r'YEAST HYDRATION (%)', value=100, min_value=1, step=1)
salt_percentage = st.number_input(r'SALT (%)', value=2, min_value=0, step=1)
hydration = st.number_input(r'DESIRABLE DOUGH HYDRATION (%)', value=80, min_value=40, max_value=120, step=1)

def calculate_water(flour, hydration, yeast, yeast_hydration):
    """
    yeast = yeast_water + yeast_flour
    = (1 + yeast_water / yeast_flour ) * yeast_flour
    = (1 + yeast_hydration / 100) * yeast_flour
    => yeast_flour = yeast / (1 + yeast_hydration / 100)
    """
    yeast_flour = yeast / (1 + yeast_hydration / 100)
    yeast_water = yeast_hydration / 100 * yeast_flour

    total_water = hydration / 100 * (flour + yeast_flour)
    water_needed = total_water - yeast_water
    return water_needed

def calculate_salt(flour, yeast, yeast_hydration, salt_percentage):
    yeast_flour = yeast / (1 + yeast_hydration / 100)
    total_flour_weight = flour + yeast_flour
    return total_flour_weight * salt_percentage / 100

st.markdown("According to the equations displayed below, the amount of water and salt required are given, respectively, by:")

water_needed = calculate_water(flour, hydration, yeast, yeast_hydration)
st.markdown(f"### Water: **{water_needed:.0f} g**")

salt_needed = calculate_salt(flour, yeast, yeast_hydration, salt_percentage)
st.markdown(f"### Salt: **{salt_needed:.0f} g**")

st.divider() 
######################################################################
st.markdown('## The Details')

st.markdown(
r"""
Let the amount of **flour** (in grams), in addition to that found in the yeast, be denoted by $F$, the amount of **yeast** (in grams) by $Y$, and the required **hydration** (as a percentage %) of the resulting dough (after including the yeast) by $H$. Furthermore, let the **yeast hydration** be denoted by $H_Y$. Finally, let the percentage of salt (as a fraction of the flour weight, $F$) be denoted by $s$. The amount of water and salt to be added, given these quantities, is determined as follows.
""")

st.markdown(" ")
######################################################################
st.markdown("### Amount of Water")

st.markdown(
r"""
The total yeast weight is usually the sum of flour, $F_Y$, and water, $W_Y$, constituents:
$$
Y = F_Y + W_Y.
$$
Let us define **yeast hydration**, $H_Y$, and the related quantity $h_Y$, as follows,
$$
H_Y = \frac{W_Y}{F_Y}\times 100,\qquad{\rm and}\qquad h_Y = \frac{W_Y}{F_Y}.
$$
The equations are more concise if we work in terms of $h_Y$ instead of $H_Y$. 
Solving for $W_Y$ in the latter equation, and substituting this into the displayed equation for $Y$, enables us to solve for the amount of flour, $F_Y$, in terms of $Y$, and $h_Y$:
$$
F_Y = \frac{Y}{1+h_Y}
$$
Substituting this equation into the displayed equation for $Y$, in turn, leads to an expression for the amount of water, $W_Y$, in the yeast in terms of $Y$ and $h_Y$,
$$
\begin{aligned}
W_Y %&= Y - \frac{Y}{1+h_Y}\\
&= \frac{h_Y}{1+h_Y}Y
\end{aligned}
$$
The total water, $W_{\rm total}$, present in the dough, given the required hydration, $H$, (written in terms of $h = H/100$) and the total flour, $F$ and $F_Y$, is:
$$
W_{\rm total} = h(F+F_Y),
$$
and since the yeast water, $W_Y$, is already present in the starter, the amount of water to be added is $W_{\rm total} - W_Y$, which, given the above, can also be written as, 
$$
\textrm{Water} = h\big(F+F_Y\big) - W_Y,
$$ 
so that, according to the above equations, the amount of water to be added is:
$$
\boxed{
\begin{aligned}
\textrm{Water} %&= h \Big(F+\frac{Y}{1+h_Y}\Big) - \frac{h_Y}{1+h_Y}Y
&= hF+ \frac{h-h_Y}{1+h_Y}Y
\end{aligned}
}
$$
"""
)

st.markdown(" ")
########################################################################
st.markdown("### Amount of Salt")

st.markdown(r"""We determine the amount of salt required by specifying a percentage, $S$, and the related quantity $s = S/100$, of salt relative to the total amount of flour. The total amount of flour is given by:
$$
F_{\rm total} = F + F_Y,
$$
and so, from above, we can also write,
$$
F_{\rm total} = F + \frac{Y}{1+h_Y}
$$
The amount of salt (in grams) to be added is then simply given by $F_{\rm total}s$, that is:
$$
\boxed{
\textrm{Salt} = \Big(F + \frac{Y}{1+h_Y}\Big)s
}
$$
""")

st.divider()
