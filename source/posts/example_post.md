---
title: "How to Write a Good Example Post"
subtitle: "Or, a Quick Walkthrough to a Bunch of HTML Tags"
author:
 - Lynn Pepin
date: 2020-09-19
lang: en-US
category: how-to
---

This is a simple static site generator. Posts are written with Markdown, and then exported to HTML and CSS. It uses Bash, Python, and relies very heavily on Pandoc. For LaTeX, it uses Mathjax and Javascript.

Pandoc does most of the heavily lifting here. The point of this was to learn a little bit of webdev, and to have more control over my static site generator.

Here's an example file for y'all.

# You should have some text, an abstract, before the first heading.

Dolores eos autem consequuntur. Aut commodi non incidunt molestias repellendus quis. Sint sapiente sit enim vitae. Labore ipsum culpa soluta quaerat tempora fugiat. Sint laborum numquam itaque sint asperiores non est saepe. Perspiciatis voluptas ut natus nulla. Eos et fugiat reprehenderit laborum expedita. Sunt sunt qui est et alias voluptatem. Dicta expedita non rem ut et. Est alias fugiat quis.

## Heading two

In this section, we look at a bunch of tags.

 * Em and strong!
 * Code tags!
 * Lists!
   * Nested lists!
   * Filler!
 * And more!

We've got all sorts of things. Double asterisks render **in this manner**, single asterisks render *in this manner*, and backticks render `in this manner`. Blocks of quotes in this manner:

```
def fizzbuzz(ii=0):
    if ii % 5 == 0:
        if % 3 == 0:
            return "Fizzbuzz!"
        return "Buzz!"
    if ii % 3 == 0:
        return "Fizz!"
    return ii
```

But what happens if we have overly long blocks?

```
fizzbuzz_oneliner = lambda ii: "Fizzbuzz!" if ii % 15 == 0 else "Fizz!" if ii % 3 == 0 else "Buzz!" if ii % 5 == 0 else ii
```

:)

We also have nested blockquotes that can be quite colorful.

> Nesting
> 
> > Nesting?
> > 
> > > Nesting!
> > >
> > > > Nesting...
> > > >
> > > > > Nesting, nesting nesting.
> > > > > 
> > > > > Words, words, words.
> > > > >
> > > > > > And more words.
> > > > >
> > > > > Yeah, those are words.
> > > >
> > 
> > I hope this gets quoted in a good blockquote!

We also have inline LaTeX $f(x) = \sqrt{\frac{1}{1-x^2}}$ and full LaTeX:

$$s(n) = \sum_{i=1}^n ||y_i - y_p||^2$$

Of course, [we also have links](https://lynndotpy.xyz). We also have numbered lists, as follows:

 1. Petunias
 2. Sunflowers
 3. Roses
 4. Tulips
 5. Not flowers:
    i. Geodes
    ii. Flooring
    iii. Sorrow
 6. Yes flowers

I'd show off headers, but they look ugly without a proper lot of text to separate them. We also have tables!


| Numbers | Words | Colors | Fake colors | Real colors |
| - | - | - | - | - |
| 1 | Hamlet   | Aubergreen   | Foggy gray | Red |
| 2 | Vampires | Lavendeen    | Not-foggy gray | `#FF0000` |
| 3 | Horatio  | Yondergrass  | Mild salmon | Scarlet |
| 4 | Lincoln  | Wintersparse | Transparent plastic | Crimson |
| 5 | Othello  | Bambigris    | Glossy plastic | Blood red |

Now let's consider something denser.

## Lorem Ipsum 2: Lorem More

Rerum id quia voluptatem dignissimos velit omnis. Perspiciatis illum sapiente nemo omnis quam veniam. Eos eaque impedit itaque commodi voluptas. Excepturi odio ex recusandae aut est sequi. Adipisci rerum sed perferendis odio cupiditate est. Tempore fuga dolorem aut eos nam.

Vel non quidem nulla qui et. Perferendis autem consequatur minus nisi rerum illum. Ut officiis eum delectus voluptas esse sed vel. Quo repellat quod eveniet velit ex magni occaecati ut. Ex nemo veritatis dolorem. Autem voluptatem molestias maxime dolorem.

Similique doloremque soluta libero ipsum ratione. Deleniti voluptatibus nihil eum aliquid ex perspiciatis maiores ipsa. Sunt dolorem quo a et sit. Dolorem similique eveniet optio perferendis molestiae ex aspernatur. Adipisci at sint at eligendi.

### Lorem Ipsum?

Lorem ipsum quia voluptatem dignissimos velit omnis. Perspiciatis illum sapiente nemo omnis quam veniam. Eos eaque impedit itaque commodi voluptas. Excepturi odio ex recusandae aut est sequi. Adipisci rerum sed perferendis odio cupiditate est. Tempore fuga dolorem aut eos nam.

Qui non inventore sequi molestias sequi aut quod nihil. Adipisci rerum doloribus non. Odio maxime recusandae omnis molestias.

Quis enim ipsum pariatur architecto magnam atque aspernatur magni. Sunt commodi eligendi autem. Ut voluptatibus laborum consequatur facilis iusto. Quidem aut dolor soluta et aut minima ex. Omnis aut omnis quaerat et ut quaerat doloribus expedita. Id maiores esse ipsum soluta quo earum.

### No, do not lorem ipsum

> Note: This section adapts content from the Wikipedia article for Lorem Ipsum. It is licensed under the "[Creative Commons Attribution-ShareAlike 3.0 Unported License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License)"

In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used before final copy is available, but it may also be used to temporarily replace copy in a process called greeking, which allows designers to consider form without the meaning of the text influencing the design.

Lorem ipsum is typically a corrupted version of De finibus bonorum et malorum, a first-century BC text by the Roman statesman and philosopher Cicero, with words altered, added, and removed to make it nonsensical, improper Latin.

Versions of the Lorem ipsum text have been used in typesetting at least since the 1960s, when it was popularized by advertisements for Letraset transfer sheets. Lorem ipsum was introduced to the digital world in the mid-1980s when Aldus employed it in graphic and word-processing templates for its desktop publishing program PageMaker. Other popular word processors including Pages and Microsoft Word have since adopted Lorem ipsum as well.

#### Example Text

A common form of Lorem ipsum reads:

> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Let's break it down.

##### Lorem

The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. Portez ce vieux whisky au juge blond qui fume. 

> 以呂波耳本部止
> 
> 千利奴流乎和加
> 
> 餘多連曽津祢那
> 
> 良牟有為能於久
> 
> 耶万計不己衣天
> 
> 阿佐伎喩女美之
> 
> 恵比毛勢須

##### Bottom text

Etaoin shrdlu cmfwyp vbgkqj xz Mavis Beacon Teaches Typing.

# Conclusion

Lorem ipsum bottom text etaoin shrdlu. I hope this article makes it useful to get an idea of how your style might look in a real article!
