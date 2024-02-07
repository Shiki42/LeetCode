class Numbers {
    constructor(private digit: number) {}

    private doesItContainDigit(nbr: number): boolean {
        if ( nbr.toString().indexOf(this.digit.toString()) !== -1) {
            return true;
        }
        return false;
    }

    public countToThousandSkip5 = (): Array<number> =>{
        let notFive: Array<number> = [];
        
        for (let i = 0; i <= 1000; i++) {
            if (i.toString().indexOf('5') !== 1){
                continue;
            }
            notFive.push(i);
        }
        
        return notFive;
    }

    set givenDigit(digit: number) {
        this.digit = digit;
    }

    get givenDigit(): number {
        return this.digit;
    }
}