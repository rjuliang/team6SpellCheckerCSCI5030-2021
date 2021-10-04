const $input = document.getElementById('input');
let INPUT_DEBOUNCE = null;

$input.addEventListener('input', e => {
    clearTimeout(INPUT_DEBOUNCE);
    $span.textContent = ''; // let's come to this on a later stage, for now pretend it doesn't exist
 
    INPUT_DEBOUNCE = setTimeout(() => main(e), 250);
});

main()

const $fakeDiv = document.getElementById('fake-div'); // used to measure space taken by the query content

const main = (e) => {
    const query = e.target.textContent.toLowerCase();
 
    if(query !== '') {
        const find_start = new Date().getTime();
     
        let parts = query.split(' ');

        const wordToComplete = parts.pop();

        rest = parts.join(' ') + ' ';

        if(wordToComplete !== '') {
             // get best match using popularity
            suggestion = getBestMatch(trie.complete(wordToComplete));

            if(suggestion) {
                $fakeDiv.innerText = query;
           
                $span.style.left = r.left + $fakeDiv.clientWidth + 'px';
               
                const ghost = suggestion.slice(wordToComplete.length);
               
                trie.clear();
           
                $span.textContent = ghost; // fill in the ghost span

                const find_end = new Date().getTime();

                const execTime = find_end - find_start;

                $time.textContent = `fetched in ${execTime}ms`;
            }
        }
        else {
            $span.textContent = ''; // clear ghost span
        }
    }
    else {
        $time.textContent = '';
        $span.textContent = ''; // clear ghost span
    }
}
const css = getComputedStyle($input);
const r = $input.getBoundingClientRect(); // to get the position, width & height of $input

const $span = document.createElement('span'); // our ghost span

$span.style.cssText = `
    width: ${r.width}px;
    height: ${r.height}px;
    left: ${r.left}px;
    top: ${r.top}px;
    z-index: -10;
    opacity: 0.4;
    position: absolute;
    white-space: pre-wrap;
    font-size: ${parseInt(css.fontSize)}px;
    padding-left: ${parseInt(css.paddingLeft)}px;
    padding-top: ${parseInt(css.paddingTop) + 1}px; // + 1 just to get a perfect alignment :p
`;

document.body.appendChild($span);

$input.addEventListener('keydown', e => {
    if(e.key === 'ArrowRight') {
        $span.textContent = ''; // clear ghost span
        $input.textContent = rest + suggestion; // fill the $input bar with required suggestion
       
        // moves cursor to the end of the input box (won't go into the details of it)
        setEndOfContenteditable($input);
    }
});