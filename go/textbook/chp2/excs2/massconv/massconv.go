// Package massconv performs various mass conversions
package massconv

import "fmt"

type Pounds float64
type Kilograms float64

func (p Pounds) String() string     { return fmt.Sprintf("%glbs", p) }
func (kg Kilograms) String() string { return fmt.Sprintf("%gkgs", kg) }

func PToKg(p Pounds) Kilograms  { return Kilograms(p / 2.20462) }
func KgToP(kg Kilograms) Pounds { return Pounds(kg * 2.20462) }
