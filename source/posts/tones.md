# Let's Brute-Force a New Musical Scale

For the purpose of this writeup, a musical **scale** is a set of frequencies that sound *good* together. Traditionally, this would be the 7 major and 5 minor keys within each octave, i.e. the classical "chromatic scale". But how did we get that, and could we follow the same principals and end up somewhere else? Spoiler alert: (1) Math, and (2) Yes!

# An intro: What are these twelve notes anyways?

This writeup is made for those who, like me, didn't know how music works. Let's start at the basics: The **octaves**.

The **octaves** are the major 'divisions' of frequencies by powers of two. Let's use 440Hz as our base frequency, since it's rather pleasant and lies near the middle of our perception of tone.

!(TODO -- logarithmic layout of octaves)

So, 110Hz, 220Hz, 440Hz, 880Hz, and 1720Hz are all spaced at roughly equal levels within human perception. We can use this as our scale! In addition to being equally spaced, these have another advantage: They are **nice ratios** of one another.

What does that mean? Well, check this out, and listen:

(TODO Image, sound)

When frequencies are nice fractions of one another (i.e. a ratio with small whole-number numerators and denominators), they'll sound nice. When they're an integer -- like two -- they'll harmonize nicely.

This is contrasted with ... todo blah blah

* Windshield wiper comparison
* Beats at near frequencies
